import csv
import io
import json
import logging

from django.db.models import ExpressionWrapper, FloatField, Func
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, reverse
from django.utils.text import slugify
from django.views import View
from django.views.generic import DetailView, FormView, ListView
from pydantic import ValidationError

from pages.forms.projects import (
    ProjectInstructionsForm,
    ProjectMeasurementsForm,
    SurveyInstructionsForm,
)
from repairs.models import Measurement, Project

LOGGER = logging.getLogger(__name__)


class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        project = self.get_object()
        context = super().get_context_data(**kwargs)

        markers = project.get_measurements_geojson()
        context["measurements"] = json.dumps(markers, default=str)

        if project.measurements.exists():
            bbox = project.get_bbox(buffer_fraction=0.1)
            centroid = project.get_centroid().coords

            context["bbox"] = list(bbox)
            context["centroid"] = list(centroid)

        return context


class ProjectMeasurementsImportView(FormView):
    form_class = ProjectMeasurementsForm
    template_name = "projects/project_measurements_form.html"

    def get_context_data(self, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs["pk"])
        stage = self.kwargs["stage"].lower()

        context = super().get_context_data(**kwargs)
        context["project"] = project
        context["stage"] = stage
        context["error"] = self.request.GET.get("error")

        if stage == "survey":
            context["is_replace"] = project.has_survey_measurements
        else:
            context["is_replace"] = project.has_production_measurements

        return context

    def get_success_url(self):
        return reverse("project-detail", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs["pk"])
        stage = self.kwargs["stage"].strip().upper()

        try:
            data = form.cleaned_data["file"].read().decode("utf-8-sig")
            with io.StringIO() as f:
                f.write(data)
                Measurement.import_from_csv(f, project=project, stage=stage)
        except ValidationError as exc:
            LOGGER.error(f"Error importing measurements: {exc}")
            redirect_url = f"{self.request.path}?error=Unable to parse the file"
            return redirect(redirect_url)

        return super().form_valid(form)


class ProjectMeasurementsExportView(View):
    """Download the project measurements CSV"""

    _columns = (
        "object_id",
        "global_id",
        "length",
        "width",
        "x",
        "y",
        "special_case",
        "quick_description",
        "h1",
        "h2",
        "linear_feet",
        "inch_feet",
        "slope",
        "curb_length",
        "survey_address",
        "surveyor",
        "note",
        "geocoded_address",
        "measured_at",
        "created_at",
    )

    def get(self, request, pk, stage):
        project = get_object_or_404(Project, pk=pk)
        filename = f"{slugify(project.name)}_measurements_{stage}.csv"
        stage = Measurement.Stage(stage.upper())

        measurements = list(
            project.measurements.filter(stage=stage)
            .order_by("object_id")
            .annotate(
                x=ExpressionWrapper(
                    Func("coordinate", function="ST_X"), output_field=FloatField()
                )
            )
            .annotate(
                y=ExpressionWrapper(
                    Func("coordinate", function="ST_Y"), output_field=FloatField()
                )
            )
            .values(*self._columns),
        )

        with io.StringIO() as f:
            writer = csv.DictWriter(f, fieldnames=self._columns)
            writer.writeheader()
            writer.writerows(measurements)

            f.seek(0)
            resp = HttpResponse(f, content_type="text/csv")
            resp["Content-Disposition"] = f'attachment; filename="{filename}"'
            return resp


class SurveyInstructionsView(FormView):
    form_class = SurveyInstructionsForm
    template_name = "projects/survey_instructions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = get_object_or_404(Project, pk=self.kwargs["pk"])
        return context


class ProjectInstructionsView(FormView):
    form_class = ProjectInstructionsForm
    template_name = "projects/project_instructions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = get_object_or_404(Project, pk=self.kwargs["pk"])
        return context
