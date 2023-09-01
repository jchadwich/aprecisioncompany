from django.shortcuts import get_object_or_404, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, FormView, UpdateView

from pages.forms.customers import CustomerProjectForm
from pss.models import Customer
from repairs.models import Project


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
    fields = ("name", "address", "city", "state")
    template_name = "customers/customer_form.html"

    def get_success_url(self):
        return reverse("customer-detail", kwargs={"pk": self.object.pk})


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ("name", "address", "city", "state")
    template_name = "customers/customer_form.html"

    def get_success_url(self):
        return reverse("customer-detail", kwargs={"pk": self.object.pk})


class CustomerProjectCreateView(FormView):
    form_class = CustomerProjectForm
    template_name = "customers/customer_project_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customer"] = get_object_or_404(Customer, pk=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse("customer-detail", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        customer = get_object_or_404(Customer, pk=self.kwargs["pk"])
        Project.objects.create(customer=customer, **form.cleaned_data)
        return super().form_valid(form)
