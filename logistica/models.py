# logistica/models.py
from django.db import models

class MaterialCampanha(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    quantidade = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=50, default="pendente")

    def __str__(self):
        return self.nome
