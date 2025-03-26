# core/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Coordenador(AbstractUser):
    # Acrescente campos extras se necessário, como telefone, departamento, etc.
    cargo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

