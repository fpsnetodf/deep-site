# marketing/urls.py
from django.urls import path
from . import views

app_name = 'marketing'

urlpatterns = [
    path('', views.lista_conteudo, name='lista'),
    path('criar/', views.criar_conteudo, name='criar'),
]
