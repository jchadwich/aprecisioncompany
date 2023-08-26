from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from django.urls import path, include


def status(request):
    """Application status/healtcheck view"""
    return JsonResponse({"status": "healthy"})


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def protected(request):
    return HttpResponse("""
        <h1>Protected</h1>
        <a href="/auth/logout/">Logout</a>
    """)


urlpatterns = [
    path("auth/login/", LoginView.as_view()),
    path("auth/logout/", LogoutView.as_view()),
    path("microsoft/", include("microsoft_auth.urls", namespace="microsoft")),
    path("admin/", admin.site.urls),
    path("status/", status),
    path("protected/", protected),
]
