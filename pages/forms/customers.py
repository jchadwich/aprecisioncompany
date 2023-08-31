from django import forms

from management.models import Customer, Project


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("name",)


class CustomerProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name", "description", "region")
