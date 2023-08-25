from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def status(request):
    """Application status/healtcheck view"""
    return JsonResponse({"status": "healthy"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("status/", status),
]
