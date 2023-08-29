from django.contrib.auth import get_user_model
from django.contrib.gis.db.models import PointField
from django.db import models

from repairs.models.constants import QuickDescription, SpecialCase
from repairs.models.management import Project

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
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)
    quick_description = models.CharField(
        max_length=10, choices=QuickDescription.choices, blank=True, null=True
    )
    special_case = models.CharField(
        max_length=10, choices=SpecialCase.choices, blank=True, null=True
    )
    h1 = models.FloatField()
    h2 = models.FloatField()
    location = PointField()
    length = models.FloatField()
    width = models.FloatField()
    lineal_feet = models.FloatField()
    inch_feet = models.FloatField()
    cost = models.FloatField()
    quality = models.FloatField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    measured_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )

    @classmethod
    def import_from_csv(cls, file_obj, project, stage, created_by=None):
        """Import a series of Measurements from a CSV file stream"""
        raise NotImplementedError


class MeasurementImage(models.Model):
    """Reference image supporting a Measurement"""

    measurement = models.ForeignKey(
        Measurement, on_delete=models.CASCADE, related_name="images"
    )
    s3_bucket = models.CharField(max_length=50)
    s3_key = models.CharField(max_length=255)
    captured_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )
