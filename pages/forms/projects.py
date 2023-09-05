from django import forms

from repairs.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "customer",
            "name",
            "description",
            "business_development_manager",
            "business_development_administrator",
            "territory",
        )
        widgets = {
            "customer": forms.HiddenInput(),
            "description": forms.TextInput(),
        }


class ProjectMeasurementsForm(forms.Form):
    """Project measurements CSV upload"""

    file = forms.FileField(widget=forms.FileInput(attrs={"accept": "text/csv"}))


class SurveyInstructionsForm(forms.Form):
    """Survey instructions form for a Project"""

    # TODO: add form fields


class ProjectInstructionsForm(forms.Form):
    """Project instructions form for a Project"""

    # TODO: add form fields
