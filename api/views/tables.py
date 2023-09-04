from rest_framework import viewsets

from pss.models import Customer
from api.serializers.tables import CustomerTableSerializer


class CustomerTableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.order_by("id")
    serializer_class = CustomerTableSerializer
