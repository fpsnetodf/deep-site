# eleitores/urls.py
from django.urls import path
from . import views

app_name = 'eleitores'

urlpatterns = [
    path('', views.eleitores_index, name='index'),
    path('cadastro/', views.cadastro_eleitor, name='cadastro'),
    path('<int:eleitor_id>/', views.eleitor_detalhe, name='detalhe'),
    path('<int:eleitor_id>/mensagem/', views.enviar_mensagem, name='enviar_mensagem'),
]
