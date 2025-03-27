# lideranca/urls.py

from django.urls import path
from . import views

app_name = 'lideranca'

urlpatterns = [
    path('', views.list_liderancas, name='list'),
    path('criar/', views.create_lideranca, name='create'),
    path('<int:pk>/', views.detail_lideranca, name='detail'),
   
    path('', views.list_liderancas, name='list'),
    path('<int:pk>/editar/', views.edit_lideranca, name='edit'),  # Nome da URL para edição
    
    # Outras rotas...
]


