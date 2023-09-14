from django import forms

from django_app.models import App


class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ("title", "code", "description")
