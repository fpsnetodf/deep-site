# logistica/models.py
from django.db import models

class MaterialCampanha(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    quantidade = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=50, default="pendente")

    def __str__(self):
        return self.nome
    
    
# Novo modelo para Rotas
class Rota(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    # Campo para armazenar os pontos da rota em formato JSON.
    # Exemplo de formato: [{"lat": -23.5, "lng": -46.6}, {"lat": -23.6, "lng": -46.7}]
    pontos = models.TextField(help_text='Insira as coordenadas em formato JSON.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome