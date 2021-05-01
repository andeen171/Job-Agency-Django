from django import forms


class HomeForm(forms.Form):
    description = forms.CharField(label="Description", max_length=1024)
