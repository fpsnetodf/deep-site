# lideranca/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Lideranca
from .forms import LiderancaForm

def list_liderancas(request):
    liderancas = Lideranca.objects.all()
    return render(request, 'lideranca/list2.html', {'liderancas': liderancas})

def create_lideranca(request):
    if request.method == 'POST':
        form = LiderancaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lideranca:list')
    else:
        form = LiderancaForm()
    return render(request, 'lideranca/create.html', {'form': form})

def detail_lideranca(request, pk):
    lideranca = get_object_or_404(Lideranca, pk=pk)
    return render(request, 'lideranca/detail.html', {'lideranca': lideranca})



def create_lideranca(request):
    if request.method == 'POST':
        form = LiderancaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lideranca:list')
    else:
        form = LiderancaForm()
    return render(request, 'lideranca/form.html', {'form': form, 'action': 'Criar'})

def edit_lideranca(request, pk):
    lideranca = get_object_or_404(Lideranca, pk=pk)
    if request.method == 'POST':
        form = LiderancaForm(request.POST, instance=lideranca)
        if form.is_valid():
            form.save()
            return redirect('lideranca:list')
    else:
        form = LiderancaForm(instance=lideranca)
    return render(request, 'lideranca/form.html', {'form': form, 'action': 'Editar'})
