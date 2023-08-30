from django.urls import path

from pages.views import index_views, organization_views, project_views


urlpatterns = [
    path("organizations/", organization_views.OrganizationListView.as_view()),
    path("organizations/<int:pk>/", organization_views.OrganizationDetailView.as_view()),
    path("projects/", project_views.ProjectListView.as_view()),
    path("projects/<int:pk>/", project_views.ProjectDetailView.as_view()),
    path("projects/<int:pk>/map/", project_views.MapView.as_view()),
    path("projects/<int:pk>/survey-instructions/", project_views.SurveyInstructionsView.as_view()),
    path("projects/<int:pk>/project-instructions/", project_views.ProjectInstructionsView.as_view()),
    path("", index_views.IndexView.as_view()),
]
