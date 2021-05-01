from django import forms


class CreateResumeForm(forms.Form):
    description = forms.CharField(label="Description", max_length=1024)
