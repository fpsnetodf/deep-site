# logistica/forms.py
from django import forms
from .models import MaterialCampanha

class MaterialCampanhaForm(forms.ModelForm):
    class Meta:
         model = MaterialCampanha
         fields = ['nome', 'descricao', 'quantidade', 'status']
         widgets = {
             'nome': forms.TextInput(attrs={'class': 'border rounded p-2'}),
             'descricao': forms.Textarea(attrs={'class': 'border rounded p-2'}),
             'quantidade': forms.NumberInput(attrs={'class': 'border rounded p-2'}),
             'status': forms.TextInput(attrs={'class': 'border rounded p-2'}),
         }
