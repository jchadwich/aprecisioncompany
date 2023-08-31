from django.urls import path

from pages.views import customer_views, index_views, project_views

urlpatterns = [
    path("customers/", customer_views.CustomerListView.as_view(), name="customer-list"),
    path(
        "customers/new/",
        customer_views.CustomerCreateView.as_view(),
        name="customer-create",
    ),
    path(
        "customers/<int:pk>/",
        customer_views.CustomerDetailView.as_view(),
        name="customer-detail",
    ),
    path("projects/", project_views.ProjectListView.as_view(), name="project-list"),
    path(
        "projects/<int:pk>/",
        project_views.ProjectDetailView.as_view(),
        name="project-detail",
    ),
    path("projects/<int:pk>/map/", project_views.MapView.as_view(), name="project-map"),
    path(
        "projects/<int:pk>/survey-instructions/",
        project_views.SurveyInstructionsView.as_view(),
        name="project-si",
    ),
    path(
        "projects/<int:pk>/project-instructions/",
        project_views.ProjectInstructionsView.as_view(),
        name="project-pi",
    ),
    path("", index_views.IndexView.as_view(), name="index"),
]
