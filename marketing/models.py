# marketing/models.py
from django.db import models

class ConteudoAudiovisual(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    data_publicacao = models.DateTimeField()
    tipo = models.CharField(max_length=50, choices=[('video', 'Vídeo'), ('fotografia', 'Fotografia')])

    def __str__(self):
        return self.titulo
