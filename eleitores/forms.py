# eleitores/forms.py
from django import forms
from .models import Eleitor, MensagemEleitor

class EleitorForm(forms.ModelForm):
    class Meta:
         model = Eleitor
         fields = ['nome', 'email', 'telefone']
         widgets = {
             'nome': forms.TextInput(attrs={'class':'border rounded p-2'}),
             'email': forms.EmailInput(attrs={'class':'border rounded p-2'}),
             'telefone': forms.TextInput(attrs={'class':'border rounded p-2'}),
         }

class MensagemEleitorForm(forms.ModelForm):
    class Meta:
         model = MensagemEleitor
         fields = ['mensagem']
         widgets = {
              'mensagem': forms.Textarea(attrs={'class':'border rounded p-2', 'placeholder':'Envie sua mensagem ao candidato'}),
         }
