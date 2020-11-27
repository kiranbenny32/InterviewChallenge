from django import forms


class RegistartionForm(forms.Form):
    team_name = forms.CharField(label='Your name', max_length=100)

