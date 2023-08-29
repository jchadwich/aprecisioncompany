from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

from repairs.models.constants import DRSpecification, Hazard, SpecialCase
from repairs.models.management import Contact, Project

User = get_user_model()


class SurveyInstructions(models.Model):
    """Survey instructions for a repair project"""

    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="si")
    primary_contact = models.ForeignKey(
        Contact,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="_si_primary",
    )
    secondary_contact = models.ForeignKey(
        Contact,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="_si_secondary",
    )
    bd = models.CharField(max_length=10)
    bda = models.CharField(max_length=10, blank=True, null=True)
    surveyor = models.CharField(max_length=10)
    needed_by = models.DateField(blank=True, null=True)
    dr_specifications = ArrayField(
        models.CharField(max_length=10, choices=DRSpecification.choices), default=list
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )


class SurveyInstructionsHazard(models.Model):
    """Survey instructions hazard entry"""

    si = models.ForeignKey(
        SurveyInstructions, on_delete=models.CASCADE, related_name="hazards"
    )
    hazard = models.CharField(max_length=10, choices=Hazard.choices)
    square_feet = models.FloatField(blank=True, null=True)
    lineal_feet = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class SurveyInstructionsSpecialCase(models.Model):
    """Survey instructions special case entry"""

    si = models.ForeignKey(
        SurveyInstructions, on_delete=models.CASCADE, related_name="special_cases"
    )
    special_case = models.CharField(max_length=10, choices=SpecialCase.choices)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class SurveyInstructionsNote(models.Model):
    """Survey instructions note"""

    si = models.ForeignKey(
        SurveyInstructions, on_delete=models.CASCADE, related_name="notes"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
