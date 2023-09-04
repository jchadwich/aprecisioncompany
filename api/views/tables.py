from rest_framework import viewsets

from api.filters.tables import CustomerTableFilter
from api.serializers.tables import CustomerTableSerializer
from pss.models import Customer


class CustomerTableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.order_by("id")
    serializer_class = CustomerTableSerializer
    filterset_class = CustomerTableFilter
