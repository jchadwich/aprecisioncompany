from django.contrib.auth import get_user_model
from django.contrib.gis.db.models import PointField
from django.db import models


User = get_user_model()


class Project(models.Model):
    """Repair project"""

    location = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=6) # TODO: validator?
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    # unique identifier?
    # name?
    # description?
    # any other information about the project?
    

class Measurement(models.Model):
    """Survey measurement for a repair project"""

    class Size(models.TextChoices):
        SMALL = ("S", "Small")
        MEDIUM = ("M", "Medium")
        LARGE = ("L", "Large")
    
    class SpecialCase(models.TextChoices):
        REPLACE = ("REPLACE", "Replace")
        CURB = ("CURB", "Curb")
        BOTTOM_HC = ("BOTTOM_HC", "Bottom HC")
        GUTTER_PAN = ("GUTTER_PAN", "Gutter Pan")
        CATCH_BASIN = ("CATCH_BASIN", "Catch Basin")
        SW2C = ("SW2C", "SW2C")
        C2B = ("C2B", "C2B")
        ASPHALT = ("ASPHALT", "Asphalt")
        DRIVEWAY = ("DRIVEWAY", "Driveway")
        LEADWALK = ("LEADWALK", "Leadwalk")

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="measurements")
    location = PointField()
    length = models.IntegerField()
    width = models.IntegerField()
    size = models.CharField(max_length=1, choices=Size.choices, blank=True, null=True)
    special_case = models.CharField(max_length=25, choices=SpecialCase.choices, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    measured_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    # h1
    # h2
    # missed
    # quality
    # accuracy
    # lineal_feet
    # inch_feet
    # cost
    # source?


class MeasurementImage(models.Model):
    """Reference image supporting a Measurement"""

    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name="images")
    s3_bucket = models.CharField(max_length=50)
    s3_key = models.CharField(max_length=255)
    captured_at = models.DateTimeField() # Timestamp from the image?
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


class SurveyInstructions(models.Model):
    """Survey instructions for a repair project"""
    # TODO: determine what/how to store everything
