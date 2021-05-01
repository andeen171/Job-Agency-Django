from django import forms


class CreateVacancyForm(forms.Form):
    description = forms.CharField(label="Description", max_length=1024)
