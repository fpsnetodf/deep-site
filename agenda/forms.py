# agenda/forms.py
from django import forms
from .models import Agenda

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['title', 'date', 'description', 'status', 'coordenador']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'border rounded p-2 w-full'}, format='%Y-%m-%d'),
            'description': forms.Textarea(attrs={'class': 'border rounded p-2 w-full', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
            'coordenador': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
        }

    def __init__(self, *args, **kwargs):
        super(AgendaForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.date:
            self.fields['date'].initial = self.instance.date.strftime('%Y-%m-%d')
