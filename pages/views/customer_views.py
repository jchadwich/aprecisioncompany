from django.views.generic import DetailView, ListView

from management.models import Customer


class CustomerListView(ListView):
    """Customer list view"""

    model = Customer
    template_name = "customers/customer_list.html"


class CustomerDetailView(DetailView):
    """Customer detail view"""

    model = Customer
    template_name = "customers/customer_detail.html"
