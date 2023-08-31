from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView

from management.models import Customer
from pages.forms.customers import CustomerForm


class CustomerListView(ListView):
    """Customer list view"""

    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"


class CustomerCreateView(FormView):
    """Customer create view"""

    template_name = "customers/customer_create.html"
    form_class = CustomerForm
    success_url = "/customers/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomerDetailView(DetailView):
    """Customer detail view"""

    model = Customer
    template_name = "customers/customer_detail.html"
    context_object_name = "customer"
