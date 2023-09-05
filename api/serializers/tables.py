from django.shortcuts import reverse
from django.utils.html import mark_safe
from rest_framework import serializers

from pss.models import Customer
from repairs.models import Project


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


class ProjectTableSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    business_development_manager = serializers.SerializerMethodField()
    business_development_administrator = serializers.SerializerMethodField()
    territory = serializers.CharField(source="territory.label")
    primary_contact = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()

    def get_name(self, obj):
        href = reverse("project-detail", kwargs={"pk": obj.pk})
        html = f'<a href="{href}">{obj.name}</a>'
        return mark_safe(html)

    def get_business_development_manager(self, obj):
        if obj.business_development_manager:
            return obj.business_development_manager.full_name
        return None

    def get_business_development_administrator(self, obj):
        if obj.business_development_administrator:
            return obj.business_development_administrator.full_name
        return None

    def get_primary_contact(self, obj):
        contact = obj.primary_contact
        if contact:
            return contact.name
        return None

    def get_created(self, obj):
        return obj.created_at.strftime("%-m/%-d/%Y")

    class Meta:
        model = Project
        fields = (
            "name",
            "business_development_manager",
            "business_development_administrator",
            "territory",
            "primary_contact",
            "created",
        )
