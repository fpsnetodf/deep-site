# core/urls.py
from django.urls import path
from . import views

app_name = 'campanha'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('campanhas/', views.list_campanhas, name='campanha_list'),
    path('campanhas/criar/', views.create_campanha, name='campanha_create'),
    path('campanhas/<int:pk>/editar/', views.edit_campanha, name='campanha_edit'),
    path('campanhas/<int:pk>/', views.detail_campanha, name='campanha_detail'),
]
