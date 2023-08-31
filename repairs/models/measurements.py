import googlemaps
from django.conf import settings
from django.contrib.gis.db.models.fields import PointField
from django.db import models, transaction

from repairs.models.constants import QuickDescription, SpecialCase
from repairs.models.projects import Project
from repairs.parsers import ProductionMeasurement, SurveyMeasurement


class Measurement(models.Model):
    """Survey measurement GIS data and metadata"""

    class Stage(models.TextChoices):
        SURVEY = ("SURVEY", "Survey")
        PRODUCTION = ("PRODUCTION", "Production")

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="measurements"
    )
    stage = models.CharField(max_length=25, choices=Stage.choices)
    object_id = models.IntegerField()
    global_id = models.UUIDField()
    coordinate = PointField()
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    special_case = models.CharField(
        max_length=10, choices=SpecialCase.choices, blank=True, null=True
    )
    quick_description = models.CharField(
        max_length=10, choices=QuickDescription.choices, blank=True, null=True
    )
    h1 = models.FloatField(blank=True, null=True)
    h2 = models.FloatField(blank=True, null=True)
    linear_feet = models.FloatField(blank=True, null=True)
    inch_feet = models.FloatField(blank=True, null=True)
    slope = models.CharField(max_length=10, blank=True, null=True)
    curb_length = models.FloatField(blank=True, null=True)
    survey_address = models.CharField(max_length=255, blank=True, null=True)
    surveyor = models.CharField(
        max_length=100, blank=True, null=True
    )  # TODO: make required
    note = models.TextField(blank=True, null=True)
    geocoded_address = models.CharField(max_length=255, blank=True, null=True)
    measured_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs):
        # FIXME: this needs to happen asynchronously (in Celery?)
        if not self.geocoded_address:
            self.geocoded_address = self.get_geocoded_address()

        return super().save(**kwargs)

    def get_geocoded_address(self):
        """Return the reverse geocoded address from the coordinate"""
        client = googlemaps.Client(key=settings.GOOGLE_API_KEY)
        addresses = client.reverse_geocode((self.coordinate.y, self.coordinate.x))

        for address in addresses:
            if address["types"] == ["premise"]:
                return address["formatted_address"]

        return None

    @staticmethod
    def import_from_csv(file_obj, project, stage):
        """Import the Measurements from CSV (replaces any existing)"""
        file_obj.seek(0)

        if stage == Measurement.Stage.SURVEY:
            parser_cls = SurveyMeasurement
        else:
            parser_cls = ProductionMeasurement

        with transaction.atomic():
            Measurement.objects.filter(project=project, stage=stage).delete()

            for data in parser_cls.from_csv(file_obj):
                kwargs = data.model_dump()
                Measurement.objects.create(project=project, stage=stage, **kwargs)

        return Measurement.objects.filter(project=project, stage=stage)


class MeasurementImage(models.Model):
    """Reference image for a Measurement"""

    measurement = models.ForeignKey(
        Measurement, on_delete=models.CASCADE, related_name="images"
    )
    url = models.URLField()
    captured_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
