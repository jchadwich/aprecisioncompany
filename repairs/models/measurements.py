from django.contrib.gis.db.models.fields import PointField
from django.db import models

from repairs.models.projects import Project
from repairs.models.constants import SpecialCase, QuickDescription


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
    surveyor = models.CharField(max_length=100, blank=True, null=True)  # creator
    note = models.TextField(blank=True, null=True)
    measured_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class MeasurementImage(models.Model):
    """Reference image for a Measurement"""

    measurement = models.ForeignKey(
        Measurement, on_delete=models.CASCADE, related_name="images"
    )
    url = models.URLField()
    captured_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
