# agenda/urls.py
from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.list_agendas, name='list'),
    path('criar/', views.create_agenda, name='create'),
    
    # Outras rotas, como edição, exclusão, etc.
]
