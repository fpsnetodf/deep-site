# logistica/urls.py
from django.urls import path
from . import views

app_name = 'logistica'

urlpatterns = [
    path('', views.lista_material, name='lista'),
    path('criar/', views.criar_material, name='criar'),    
    path('rotas/', views.list_rotas, name='rota_list'),
    path('rotas/criar/', views.create_rota, name='rota_create'),
    path('rotas/<int:pk>/', views.rota_detail, name='rota_detail'),
]
