from django.urls import path

from . import views

urlpatterns = [
    path('docgen', views.docgen, name='docgen')
]