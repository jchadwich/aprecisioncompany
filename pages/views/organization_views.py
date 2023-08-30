from django.views.generic import DetailView, ListView

from management.models import Organization


class OrganizationListView(ListView):
    """Organization list view"""
    model = Organization
    template_name = "organizations/organization_list.html"


class OrganizationDetailView(DetailView):
    """Organization detail view"""
    model = Organization
    template_name = "organizations/organization_detail.html"
