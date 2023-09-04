import django_filters

from pss.models import Customer


class CustomerTableFilter(django_filters.FilterSet):
    """Customer data table filters"""

    q = django_filters.CharFilter(method="filter_q")

    def filter_q(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

    class Meta:
        model = Customer
        fields = ("q",)
