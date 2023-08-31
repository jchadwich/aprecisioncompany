from django.contrib.auth import get_user_model
from django.contrib.gis.db.models import PointField
from django.db import models, transaction

from management.models import Project
from repairs.models.constants import QuickDescription, SpecialCase
from repairs.parsers import MeasurementParser

User = get_user_model()


class Measurement(models.Model):
    """Survey measurement for a repair project"""

    class Stage(models.TextChoices):
        # FIXME: check for the appropriate choices
        INITIAL = ("INITIAL", "Initial")
        FINAL = ("FINAL", "Final")

    object_id = models.IntegerField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="measurements"
    )
    stage = models.CharField(max_length=10, choices=Stage.choices)
    survey_address = models.CharField(max_length=255, blank=True, null=True)
    # city = models.CharField(max_length=100, blank=True, null=True)
    # state = models.CharField(max_length=2, blank=True, null=True)
    # country = models.CharField(max_length=50, blank=True, null=True)
    # zip_code = models.CharField(max_length=6, blank=True, null=True)
    quick_description = models.CharField(
        max_length=10, choices=QuickDescription.choices, blank=True, null=True
    )
    special_case = models.CharField(
        max_length=10, choices=SpecialCase.choices, blank=True, null=True
    )
    h1 = models.FloatField(blank=True, null=True)
    h2 = models.FloatField(blank=True, null=True)
    location = PointField()
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    # lineal_feet = models.FloatField()
    # inch_feet = models.FloatField()
    # cost = models.FloatField()
    # quality = models.FloatField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    measured_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )

    # TODO: curb length?

    @staticmethod
    def import_from_csv(file_obj, project, stage, created_by=None):
        """Import a series of Measurements from a CSV file stream"""
        with transaction.atomic():
            # Delete any measurements for the project with the same stage since
            # any new CSV imports are replacements.
            Measurement.objects.filter(project=project, stage=stage).delete()

            # Parse each CSV row and insert the record
            parser = MeasurementParser()
            for kwargs in parser.parse(file_obj):
                kwargs["project"] = project
                kwargs["stage"] = stage
                kwargs["created_by"] = created_by
                images = kwargs.pop("images")

                measurement = Measurement.objects.create(**kwargs)

                for image in images:
                    MeasurementImage.objects.create(measurement=measurement, **image)

        return Measurement.objects.filter(project=project, stage=stage)


class MeasurementImage(models.Model):
    """Reference image supporting a Measurement"""

    measurement = models.ForeignKey(
        Measurement, on_delete=models.CASCADE, related_name="images"
    )
    url = models.URLField(max_length=255)
    captured_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
