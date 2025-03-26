# lideranca/forms.py

from django import forms
from .models import Lideranca

class LiderancaForm(forms.ModelForm):
    class Meta:
        model = Lideranca
        fields = ['nome', 'email', 'metas', 'campanha']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'email': forms.EmailInput(attrs={'class': 'border rounded p-2 w-full'}),
            'metas': forms.Textarea(attrs={'class': 'border rounded p-2 w-full', 'rows': 3}),
            'campanha': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
        }
