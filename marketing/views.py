# marketing/views.py
from django.shortcuts import render, redirect
from .models import ConteudoAudiovisual
from .forms import ConteudoAudiovisualForm

def lista_conteudo(request):
    conteudos = ConteudoAudiovisual.objects.all().order_by('-data_publicacao')
    return render(request, 'marketing/lista.html', {'conteudos': conteudos})

def criar_conteudo(request):
    if request.method == 'POST':
         form = ConteudoAudiovisualForm(request.POST)
         if form.is_valid():
              form.save()
              return redirect('marketing:lista')
    else:
         form = ConteudoAudiovisualForm()
    return render(request, 'marketing/criar.html', {'form': form})

