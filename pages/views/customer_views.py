from django.shortcuts import get_object_or_404, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView

from management.models import Customer, Project
from pages.forms.customers import CustomerForm, CustomerProjectForm


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


class CustomerProjectCreate(FormView):
    """Project create view for a Customer"""

    form_class = CustomerProjectForm
    template_name = "customers/customer_project_create.html"

    def get(self, request, pk):
        get_object_or_404(Customer, pk=pk)
        return super().get(request, pk)

    def get_success_url(self):
        """Return the URL to redirect to on success"""
        return reverse("project-detail", kwargs={"pk": self.project.pk})

    def form_valid(self, form):
        customer = get_object_or_404(Customer, pk=self.kwargs["pk"])
        self.project = Project.objects.create(customer=customer, **form.cleaned_data)
        return super().form_valid(form)
