from django import forms

from repairs.models import Project


class CustomerProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "business_development_manager",
            "business_development_administrator",
            "territory",
        )
        widgets = {
            "description": forms.TextInput(),
        }
