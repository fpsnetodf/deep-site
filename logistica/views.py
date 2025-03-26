# logistica/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import MaterialCampanha, Rota
from .forms import MaterialCampanhaForm, RotaForm

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


# VIEW: Listar rotas
def list_rotas(request):
    rotas = Rota.objects.all().order_by('nome')
    return render(request, 'logistica/rotas/list.html', {'rotas': rotas})

# VIEW: Criar nova rota
def create_rota(request):
    if request.method == "POST":
        form = RotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logistica:rota_list')
    else:
        form = RotaForm()
    return render(request, 'logistica/rotas/form.html', {'form': form, 'action': 'Criar'})

# VIEW: Detalhes da rota (incluindo mapa com Leaflet)
def rota_detail(request, pk):
    rota = get_object_or_404(Rota, pk=pk)
    return render(request, 'logistica/rotas/detail.html', {'rota': rota})



