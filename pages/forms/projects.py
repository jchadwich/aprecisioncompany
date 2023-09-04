from django import forms


class ProjectMeasurementsForm(forms.Form):
    """Project measurements CSV upload"""

    file = forms.FileField(widget=forms.FileInput(attrs={"accept": "text/csv"}))


class SurveyInstructionsForm(forms.Form):
    """Survey instructions form for a Project"""

    # TODO: add form fields


class ProjectInstructionsForm(forms.Form):
    """Project instructions form for a Project"""

    # TODO: add form fields
