from rest_framework import viewsets

from api.filters.tables import CustomerTableFilter, ProjectTableFilter
from api.serializers.tables import CustomerTableSerializer, ProjectTableSerializer
from pss.models import Customer
from repairs.models import Project


class CustomerTableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.order_by("id")
    serializer_class = CustomerTableSerializer
    filterset_class = CustomerTableFilter


class ProjectTableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.order_by("id")
    serializer_class = ProjectTableSerializer
    filterset_class = ProjectTableFilter
