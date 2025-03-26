# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
    return render(request, 'dashboard/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login:login')

def sobre(request):
    return render(request, 'sobre/sobre.html')

def contato(request):
    return render(request, 'contato/contato.html')

