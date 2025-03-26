# eleitores/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Eleitor
from .forms import EleitorForm, MensagemEleitorForm

def eleitores_index(request):
    eleitores = Eleitor.objects.all()
    return render(request, 'eleitores/index.html', {'eleitores': eleitores})

def cadastro_eleitor(request):
    if request.method == 'POST':
         form = EleitorForm(request.POST)
         if form.is_valid():
              form.save()
              return redirect('eleitores:index')
    else:
         form = EleitorForm()
    return render(request, 'eleitores/cadastro.html', {'form': form})

def eleitor_detalhe(request, eleitor_id):
    eleitor = get_object_or_404(Eleitor, id=eleitor_id)
    mensagens = eleitor.mensagens.all().order_by('-enviado_em')
    return render(request, 'eleitores/detalhe.html', {'eleitor': eleitor, 'mensagens': mensagens})

def enviar_mensagem(request, eleitor_id):
    eleitor = get_object_or_404(Eleitor, id=eleitor_id)
    if request.method == 'POST':
         form = MensagemEleitorForm(request.POST)
         if form.is_valid():
              mensagem = form.save(commit=False)
              mensagem.eleitor = eleitor
              mensagem.save()
              return redirect('eleitores:detalhe', eleitor_id=eleitor.id)
    else:
         form = MensagemEleitorForm()
    return render(request, 'eleitores/enviar_mensagem.html', {'form': form, 'eleitor': eleitor})

