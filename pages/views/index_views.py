from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Application root index view"""

    template_name = "index/index.html"
