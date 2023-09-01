from django.urls import path

from pages.views import index_views, customer_views, project_views, map_views


urlpatterns = [
    path("customers/", customer_views.CustomerListView.as_view(), name="customer-list"),
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
    path("map/", map_views.MapView.as_view(), name="map"),
    path("", index_views.IndexView.as_view(), name="index"),
]
