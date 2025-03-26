# logistica/urls.py
from django.urls import path
from . import views

app_name = 'logistica'

urlpatterns = [
    path('', views.lista_material, name='lista'),
    path('criar/', views.criar_material, name='criar'),
]
