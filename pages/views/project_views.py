from django.views.generic import ListView, DetailView

from management.models import Project


class ProjectListView(ListView):
    """Project list view"""

    model = Project
    template_name = "projects/project_list.html"


class ProjectDetailView(DetailView):
    """Project detail view"""

    model = Project
    template_name = "projects/project_detail.html"


class MapView(DetailView):
    """Project map view"""

    model = Project
    template_name = "projects/map.html"


class SurveyInstructionsView(DetailView):
    """Project survery instructions view"""

    model = Project
    template_name = "projects/survey_instructions.html"


class ProjectInstructionsView(DetailView):
    """Project project instructions view"""

    model = Project
    template_name = "projects/project_instructions.html"
