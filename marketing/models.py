# marketing/models.py
from django.db import models

class ConteudoAudiovisual(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    data_publicacao = models.DateTimeField()
    tipo = models.CharField(max_length=50, choices=[('video', 'Vídeo'), ('fotografia', 'Fotografia')])

    def __str__(self):
        return self.titulo


# class MaterialCampanha(models.Model):
#     nome = models.CharField(max_length=255)
#     tipo = models.CharField(max_length=50, choices=[('grafico', 'Gráfico'), ('audiovisual', 'Audiovisual')])
#     quantidade = models.IntegerField()
#     aprovado = models.BooleanField(default=False)

#     def __str__(self):
#         return self.nome