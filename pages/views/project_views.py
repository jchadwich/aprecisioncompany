from django.views.generic import DetailView, FormView, ListView

from pages.forms.projects import ProjectInstructionsForm, SurveyInstructionsForm
from repairs.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"


class SurveyInstructionsView(FormView):
    form_class = SurveyInstructionsForm
    template_name = "projects/survey_instructions.html"


class ProjectInstructionsView(FormView):
    form_class = ProjectInstructionsForm
    template_name = "projects/project_instructions.html"
