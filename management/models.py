from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Region(models.Model):
    """Geographical region to classify Projects"""

    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Organization(models.Model):
    """External municipality or customer for project grouping"""

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Project(models.Model):
    """Independent project for an Organization"""

    # TODO: status?
    # TODO: primary/secondary contacts?
    # TODO: BD/BDA?

    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="projects"
    )
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    """Contact information for an external person"""

    # TODO: organization?

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    extension = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
