from rest_framework import viewsets

from api.filters.tables import (
    ContactTableFilter,
    CustomerTableFilter,
    ProjectTableFilter,
)
from api.serializers.tables import (
    ContactTableSerializer,
    CustomerTableSerializer,
    ProjectTableSerializer,
)
from pss.models import Contact, Customer
from repairs.models import Project


class ContactTableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.order_by("id")
    serializer_class = ContactTableSerializer
    filterset_class = ContactTableFilter


class CustomerTableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.order_by("id")
    serializer_class = CustomerTableSerializer
    filterset_class = CustomerTableFilter


class ProjectTableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.order_by("id")
    serializer_class = ProjectTableSerializer
    filterset_class = ProjectTableFilter
