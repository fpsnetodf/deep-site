# campanha/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

# def login_view(request):
#     if request.method == 'POST':
#          username = request.POST.get('username')
#          password = request.POST.get('password')
#          user = authenticate(request, username=username, password=password)
#          if user is not None:
#               login(request, user)
#               return redirect('campanha:dashboard')
#          else:
#               error = "Usuário ou senha inválidos."
#               return render(request, 'login/login.html', {'error': error})
#     return render(request, 'login/login.html')

# @login_required
# def dashboard(request):
#     return render(request, 'dashboard/dashboard.html')

# def logout_view(request):
#     logout(request)
#     return redirect('login:login')

# def sobre(request):
#     return render(request, 'sobre/sobre.html')

# def contato(request):
#     return render(request, 'contato/contato.html')

# campanha/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from campanha.models import Campanha  # Se precisar de campanha, por exemplo
from agenda.models import Agenda  # Se precisar usar as agendas para algum dado
from lideranca.models import Lideranca
# campanha/views.py
from .forms import CampanhaForm

def login_view(request):
    if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username=username, password=password)
         if user is not None:
              login(request, user)
              return redirect('campanha:dashboard')
         else:
              error = "Usuário ou senha inválidos."
              return render(request, 'login/login.html', {'error': error})
    return render(request, 'login/login.html')



@login_required
def dashboard(request):
    noticias = [
        {"titulo": "Evento marcado para amanhã!", "url": "/agenda/"},
        {"titulo": "Nova liderança cadastrada.", "url": "/lideranca/"},
        {"titulo": "Confira as atualizações de Logística", "url": "/logistica/"},
        {"titulo": "Novidades em Marketing", "url": "/marketing/"}
    ]
    liderancas = None
    try:
        from lideranca.models import Lideranca
        liderancas = Lideranca.objects.all()
    except ImportError:
        liderancas = []

    context = {
        'noticias': noticias,
        'liderancas': liderancas,
    }
    return render(request, 'dashboard/dashboard.html', context)

def sobre(request):
    return render(request, 'sobre/sobre.html')

def contato(request):
    return render(request, 'contato/contato.html')

def logout_view(request):
    logout(request)
    return redirect('campanha:login')

def list_campanhas(request):
    campanhas = Campanha.objects.all()
    return render(request, 'campanha/campanha_list.html', {'campanhas': campanhas})

def create_campanha(request):
    if request.method == 'POST':
        form = CampanhaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campanha:campanha_list')
    else:
        form = CampanhaForm()
    return render(request, 'campanha/campanha_form.html', {'form': form})

def edit_campanha(request, pk):
    campanha = get_object_or_404(Campanha, pk=pk)
    if request.method == 'POST':
        form = CampanhaForm(request.POST, instance=campanha)
        if form.is_valid():
            form.save()
            return redirect('campanha:campanha_list')
    else:
        form = CampanhaForm(instance=campanha)
    return render(request, 'campanha/campanha_form.html', {'form': form})

def detail_campanha(request, pk):
    campanha = get_object_or_404(Campanha, pk=pk)
    return render(request, 'campanha/campanha_detail.html', {'campanha': campanha})