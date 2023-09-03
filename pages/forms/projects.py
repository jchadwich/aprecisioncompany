import os

from django import forms


def validate_csv(file_obj):
    """Validate the file extension is a CSV"""
    _, ext = os.path.splitext(file_obj.name)
    return ext.strip().lower() == ".csv"


class ProjectMeasurementsForm(forms.Form):
    """Project measurements CSV upload"""

    file = forms.FileField(validators=[validate_csv])


class SurveyInstructionsForm(forms.Form):
    """Survey instructions form for a Project"""

    # TODO: add form fields


class ProjectInstructionsForm(forms.Form):
    """Project instructions form for a Project"""

    # TODO: add form fields
