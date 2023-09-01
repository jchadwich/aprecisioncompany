from django.db import models


class Customer(models.Model):
    """External client or municipality"""

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    """Contact information for an external person"""

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="contacts"
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Territory(models.Model):
    """Categorical geographic region/territory"""

    name = models.CharField(max_length=100, unique=True)
    label = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
