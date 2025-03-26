from django.db import models 
from campanha.models import Campanha


class Lideranca(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    metas = models.TextField()
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, related_name="liderancas")

    def __str__(self):
        return self.nome
