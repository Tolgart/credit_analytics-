from django import forms

from clients.models import CorporateClient


class CorporateClientForm(forms.ModelForm):
    class Meta:
        model = CorporateClient
        fields = ['name', 'inn', 'industry', 'registration_date', 'is_active']
        widgets = {
            'registration_date': forms.DateInput(attrs={'type': 'date'}),
        }