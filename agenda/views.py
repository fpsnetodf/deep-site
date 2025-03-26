# agenda/views.py
# from django.shortcuts import render
# from .models import Agenda




# agenda/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Agenda
from .forms import AgendaForm

# @login_required
def list_agendas(request):
    agendas = Agenda.objects.all().order_by('date')
    return render(request, 'agenda/list2.html', {'agendas': agendas})

@login_required
def create_agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            agenda = form.save(commit=False)
            agenda.created_by = request.user
            agenda.save()
            return redirect('agenda:list')
    else:
        form = AgendaForm()
    return render(request, 'agenda/create.html', {'form': form})

# def list_agendas(request):
#     agendas = Agenda.objects.all().order_by('date')
#     return render(request, 'agenda/list.html', {'agendas': agendas})