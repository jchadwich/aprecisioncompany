from django.http import JsonResponse
from django.views.generic import TemplateView


def status(request):
    """Application status/healtcheck view"""
    return JsonResponse({"status": "healthy"})


class IndexView(TemplateView):
    """Index page template view"""
    template_name = "core/index.html"
