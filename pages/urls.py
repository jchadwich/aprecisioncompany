from django.urls import path

from pages.views import index_views, organization_views, project_views


urlpatterns = [
    path("organizations/", organization_views.OrganizationListView.as_view(), name="organization-list"),
    path("organizations/<int:pk>/", organization_views.OrganizationDetailView.as_view(), name="organization-detail"),
    path("projects/", project_views.ProjectListView.as_view(), name="project-list"),
    path("projects/<int:pk>/", project_views.ProjectDetailView.as_view(), name="project-detail"),
    path("projects/<int:pk>/map/", project_views.MapView.as_view(), name="project-map"),
    path("projects/<int:pk>/survey-instructions/", project_views.SurveyInstructionsView.as_view(), name="project-si"),
    path("projects/<int:pk>/project-instructions/", project_views.ProjectInstructionsView.as_view(), name="project-pi"),
    path("", index_views.IndexView.as_view(), name="index"),
]
