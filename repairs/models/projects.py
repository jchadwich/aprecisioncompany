from django.contrib.auth import get_user_model
from django.db import models

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

    @property
    def primary_contact(self):
        """Return the primary Contact (if exists)"""
        return self.contacts.order_by("projectcontact__order").first()


class ProjectContact(models.Model):
    """Through table for the Project/Contact relationship"""

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
