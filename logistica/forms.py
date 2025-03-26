# logistica/forms.py
from django import forms
from .models import MaterialCampanha, Rota

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

# Formulário para cadastro de Rotas
class RotaForm(forms.ModelForm):
    class Meta:
        model = Rota
        fields = ['nome', 'descricao', 'pontos']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'descricao': forms.Textarea(attrs={'class': 'border rounded p-2 w-full', 'rows': 3}),
            # Se desejar que o campo fique oculto (pois será preenchido via script):
            'pontos': forms.Textarea(attrs={
                'class': 'border rounded p-2 w-full',
                'rows': 5,
                'placeholder': 'Clique no mapa para definir a rota...',
                'style': 'display: none;'
            }),
        }