from django.contrib.auth import get_user_model
from django.contrib.gis.db.models.aggregates import Union
from django.db import models, transaction

from pss.models import Contact, Customer, Territory

User = get_user_model()


class Project(models.Model):
    """Repair project for a Customer"""

    class Status(models.TextChoices):
        """Status choices"""

        STARTED = ("S", "Started")
        IN_PROGRESS = ("I", "In Progress")
        COMPLETE = ("C", "Complete")
        CANCELED = ("X", "Canceled")

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=1, choices=Status.choices, default=Status.STARTED
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="projects"
    )
    business_development_manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="bd_projects",
    )
    business_development_administrator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="bda_projects",
    )
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)
    contacts = models.ManyToManyField(
        Contact, through="ProjectContact", through_fields=("project", "contact")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def primary_contact(self):
        """Return the primary Contact (if exists)"""
        return self.contacts.filter(projectcontact__order=0).first()

    @property
    def secondary_contact(self):
        """Return the secondary Contact (if exists)"""
        return self.contacts.filter(projectcontact__order=1).first()

    def get_bbox(self, buffer_fraction=0):
        """Return the bounding box of the Measurements"""
        union = self.measurements.aggregate(union=Union("coordinate"))["union"]
        bbox = union.extent

        if buffer_fraction:
            (xmin, ymin, xmax, ymax) = bbox
            buffer = buffer_fraction * max(xmax - xmin, ymax - ymin)
            bbox = union.buffer(buffer).extent

        return bbox

    def get_centroid(self):
        """Return the centroid of the Measurements"""
        union = self.measurements.aggregate(union=Union("coordinate"))["union"]
        return union.centroid

    def get_measurements_geojson(self):
        """Return the GeoJSON dictionary of the Measurements"""
        from api.serializers.measurements import MeasurementSerializer

        measurements = self.measurements.all()
        serializer = MeasurementSerializer(measurements, many=True)
        return serializer.data

    def get_survey_measurements(self):
        """Return the survey measurements queryset"""
        from repairs.models.measurements import Measurement

        stage = Measurement.Stage.SURVEY
        return self.measurements.filter(stage=stage)

    @property
    def has_survey_measurements(self):
        """Return True if the survey measurements exist"""
        return self.get_survey_measurements().exists()

    def get_production_measurements(self):
        """Return the production measurements queryset"""
        from repairs.models.measurements import Measurement

        stage = Measurement.Stage.PRODUCTION
        return self.measurements.filter(stage=stage)

    @property
    def has_production_measurements(self):
        """Return True if the production measurements exist"""
        return self.get_production_measurements().exists()

    @property
    def has_survey_instructions(self):
        """Return True if the survey instructions exist"""
        # TODO: define logic
        return False

    @property
    def has_project_instructions(self):
        """Return True if the project instructions exist"""
        # TODO: define logic
        return False

    @property
    def has_pricing_sheet(self):
        """Return True if the pricing sheet exists"""
        # TODO: define logic
        return False

    @property
    def has_project_summary(self):
        """Return True if the project summary exists"""
        # TODO: define logic
        return False

    @property
    def has_post_project_review(self):
        """Return True if the post-project review exists"""
        # TODO: define logic
        return False

    def set_contact(self, contact, order=0):
        """Set a Project's contact"""
        with transaction.atomic():
            ProjectContact.objects.filter(project=self, order=order).delete()

            if contact:
                ProjectContact.objects.create(
                    project=self, contact=contact, order=order
                )


class ProjectContact(models.Model):
    """Through table for the Project/Contact relationship"""

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.name} - {self.contact.name} - {self.order}"
