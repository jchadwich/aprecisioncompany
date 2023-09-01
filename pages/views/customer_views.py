from django.shortcuts import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from pss.models import Customer


# TODO: handle pagination
class CustomerListView(ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"

    def get_queryset(self):
        return Customer.objects.order_by("created_at")


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"
    context_object_name = "customer"


class CustomerCreateView(CreateView):
    model = Customer
    fields = ("name",)
    template_name = "customers/customer_create.html"

    def get_success_url(self):
        return reverse("customer-detail", kwargs={"pk": self.object.pk})


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ("name",)
    template_name = "customers/customer_update.html"

    def get_success_url(self):
        return reverse("customer-detail", kwargs={"pk": self.object.pk})
