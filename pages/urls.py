from django.urls import path

from pages.views import customer_views, index_views, map_views, project_views

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
    path(
        "customers/<int:pk>/edit/",
        customer_views.CustomerUpdateView.as_view(),
        name="customer-update",
    ),
    path(
        "customers/<int:pk>/projects/new/",
        customer_views.CustomerProjectCreateView.as_view(),
        name="customer-project-create",
    ),
    path("projects/", project_views.ProjectListView.as_view(), name="project-list"),
    path(
        "projects/<int:pk>/",
        project_views.ProjectDetailView.as_view(),
        name="project-detail",
    ),
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
    path("map/", map_views.MapView.as_view(), name="map"),
    path("", index_views.IndexView.as_view(), name="index"),
]
