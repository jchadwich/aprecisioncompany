from django.utils.html import mark_safe
from django.shortcuts import reverse
from rest_framework import serializers

from pss.models import Customer


class CustomerTableSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    active_projects = serializers.SerializerMethodField()
    completed_projects = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()

    def get_name(self, obj):
        href = reverse("customer-detail", kwargs={"pk": obj.pk})
        html = f'<a href="{href}">{obj.name}</a>'
        return mark_safe(html)

    def get_location(self, obj):
        return obj.short_address or ""

    def get_active_projects(self, obj):
        return obj.active_projects.count()

    def get_completed_projects(self, obj):
        return obj.completed_projects.count()

    def get_created(self, obj):
        return obj.created_at.strftime("%-m/%-d/%Y")

    class Meta:
        model = Customer
        fields = (
            "name",
            "location",
            "active_projects",
            "completed_projects",
            "created",
        )
