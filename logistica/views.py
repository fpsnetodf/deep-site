# logistica/views.py
from django.shortcuts import render, redirect
from .models import MaterialCampanha
from .forms import MaterialCampanhaForm

def lista_material(request):
    materiais = MaterialCampanha.objects.all()
    return render(request, 'logistica/lista.html', {'materiais': materiais})

def criar_material(request):
    if request.method == 'POST':
         form = MaterialCampanhaForm(request.POST)
         if form.is_valid():
              form.save()
              return redirect('logistica:lista')
    else:
         form = MaterialCampanhaForm()
    return render(request, 'logistica/criar.html', {'form': form})
