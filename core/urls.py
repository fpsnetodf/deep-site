from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', include('campanha.urls')),        # Páginas institucionais e dashboard
    path('agenda/', include('agenda.urls')), # Gestão de agendas
    path('eleitores/', include('eleitores.urls')), # Cadastro/mensagens dos eleitores
    path('logistica/', include('logistica.urls')), # Gestão de materiais e logística
    path('marketing/', include('marketing.urls')), # Conteúdo e redes sociais
]
