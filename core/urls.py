from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Inclui as URLs padrão do Django
    path('', include('campanha.urls')),        # Páginas institucionais e dashboard
    path('agenda/', include('agenda.urls')), # Gestão de agendas
    path('eleitores/', include('eleitores.urls')), # Cadastro/mensagens dos eleitores
    path('logistica/', include('logistica.urls')), # Gestão de materiais e logística
    path('marketing/', include('marketing.urls')), # Conteúdo e redes sociais
    path('lideranca/', include('lideranca.urls')),  # Aqui você integra as URLs de liderança.
]
