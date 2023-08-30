from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Region(models.Model):
    """Geographical region to classify Projects"""

    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    """External municipality or customer for project grouping"""

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    """Contact information for an external person"""

    name = models.CharField(max_length=100)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="contacts"
    )
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    extension = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Project(models.Model):
    """Independent project for an Customer"""

    # TODO: status?
    # TODO: primary/secondary contacts?
    # TODO: BD/BDA?

    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="projects"
    )
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True)
    contacts = models.ManyToManyField(
        Contact, through="ProjectContact", through_fields=("project", "contact")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def has_contact(self, contact):
        """Return True if the Project has the Contact"""
        return self.contacts.filter(pk=contact.pk).exists()

    def insert_contact(self, contact, order=None):
        """Insert a new Contact for the Project"""
        if not self.has_contact(contact):
            if order is None:
                order = self.contacts.count()

            ProjectContact.objects.create(project=self, contact=contact, order=order)

    def remove_contact(self, contact):
        """Remove a Contact from the Project"""
        self.contacts.filter(pk=contact.pk).delete()
        contacts = self.contacts.order_by("order")
        self.reorder_contacts(contacts)

    def reorder_contacts(self, contacts):
        """Reorder the Contacts in the Project according to the list"""
        order = 0

        for index, contact in enumerate(contacts):
            if not self.has_contact(contact):
                continue

            record = ProjectContact.objects.get(project=self, contact=contact)
            record.order = order
            record.save()

            order += 1


class ProjectContact(models.Model):
    """Contacts for each Project (through table)"""

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("project", "contact")
