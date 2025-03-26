# core/forms.py

from django import forms
from .models import Campanha

class CampanhaForm(forms.ModelForm):
    class Meta:
        model = Campanha
        fields = ['nome', 'descricao', 'data_inicio', 'data_fim']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'descricao': forms.Textarea(attrs={'class': 'border rounded p-2 w-full', 'rows': 3}),
            'data_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'border rounded p-2 w-full'}),
            'data_fim': forms.DateInput(attrs={'type': 'date', 'class': 'border rounded p-2 w-full'}),
        }
