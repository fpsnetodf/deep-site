# agenda/urls.py
from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.list_agendas, name='list'),
    path('criar/', views.create_agenda, name='create'),
    path('<int:pk>/', views.detail_agenda, name='detail'),
    path('<int:pk>/editar/', views.edit_agenda, name='edit'),
    path('<int:pk>/excluir/', views.delete_agenda, name='delete'),
]

