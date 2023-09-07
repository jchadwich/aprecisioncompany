from django.contrib import admin

from repairs.models import Project, ProjectContact, Measurement, MeasurementImage


admin.site.register(Measurement)
admin.site.register(MeasurementImage)
admin.site.register(Project)
admin.site.register(ProjectContact)
