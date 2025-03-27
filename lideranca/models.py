from django.db import models 
from campanha.models import Campanha


# class Lideranca(models.Model):
#     nome = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     metas = models.TextField()
#     campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, related_name="liderancas")

#     def __str__(self):
#         return self.nome


# lideranca/models.py
# from django.db import models

# class Lideranca(models.Model):
#     nome = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     metas = models.TextField()
#     campanhas = models.ManyToManyField("campanha.Campanha", related_name="liderancas")

#     def __str__(self):
#         return self.nome

from django.db import models
from campanha.models import Campanha  # Certifique-se de que o modelo Campanha está importado

class Lideranca(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    campanhas = models.ManyToManyField(Campanha, related_name="liderancas")

    def __str__(self):
        return self.nome

