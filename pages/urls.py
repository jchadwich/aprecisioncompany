from django.urls import path

from pages.views import index_views


urlpatterns = [
    path("", index_views.IndexView.as_view(), name="index"),
]
