# marketing/forms.py
from django import forms
from .models import ConteudoAudiovisual

class ConteudoAudiovisualForm(forms.ModelForm):
    class Meta:
         model = ConteudoAudiovisual
         fields = ['titulo', 'descricao', 'data_publicacao', 'tipo']
         widgets = {
             'titulo': forms.TextInput(attrs={'class': 'border rounded p-2'}),
             'descricao': forms.Textarea(attrs={'class': 'border rounded p-2'}),
             'data_publicacao': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'border rounded p-2'}),
             'tipo': forms.Select(attrs={'class': 'border rounded p-2'}),
         }
