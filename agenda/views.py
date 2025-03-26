# agenda/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agenda
from .forms import AgendaForm

@login_required
def list_agendas(request):
    agendas = Agenda.objects.all().order_by('date') # Use 'date' em vez de 'data'
    return render(request, 'agenda/list4.html', {'agendas': agendas})

@login_required
def create_agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:list')
    else:
        form = AgendaForm()
    return render(request, 'agenda/form.html', {'form': form})

@login_required
def detail_agenda(request, pk):
    agenda = get_object_or_404(Agenda, pk=pk)
    return render(request, 'agenda/detail.html', {'agenda': agenda})

@login_required
def edit_agenda(request, pk):
    agenda = get_object_or_404(Agenda, pk=pk)
    if request.method == 'POST':
        form = AgendaForm(request.POST, instance=agenda)
        if form.is_valid():
            form.save()
            return redirect('agenda:detail', pk=agenda.pk)
    else:
        form = AgendaForm(instance=agenda)
    return render(request, 'agenda/form.html', {'form': form, 'action': 'Editar'})

@login_required
def delete_agenda(request, pk):
    agenda = get_object_or_404(Agenda, pk=pk)
    if request.method == 'POST':
        agenda.delete()
        return redirect('agenda:list')
    return render(request, 'agenda/confirm_delete.html', {'agenda': agenda})

