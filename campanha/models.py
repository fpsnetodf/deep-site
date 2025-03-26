from django.contrib.auth.models import AbstractUser
from django.db import models

class Campanha(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome

# class Coordenador(models.Model):
#     nome = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     telefone = models.CharField(max_length=15)
#     campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, related_name="coordenadores")

#     def __str__(self):
#         return self.nome

class Coordenador(AbstractUser):
    cargo = models.CharField(max_length=100, blank=True)
    REQUIRED_FIELDS = []  # Se desejar, adicione campos obrigatórios, como 'email', por exemplo.

    def __str__(self):
        return self.username