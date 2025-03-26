# agenda/forms.py
from django import forms
from .models import Agenda

class AgendaForm(forms.ModelForm):
    class Meta:
         model = Agenda
         fields = ['title', 'description', 'date', 'status']
         widgets = {
             'date': forms.DateTimeInput(attrs={
                 'type': 'datetime-local', 
                 'class': 'border rounded p-2'
             }),
             'title': forms.TextInput(attrs={'class': 'border rounded p-2'}),
             'description': forms.Textarea(attrs={'class': 'border rounded p-2'}),
             'status': forms.Select(attrs={'class': 'border rounded p-2'}),
         }
