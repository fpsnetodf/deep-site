# eleitores/models.py
from django.db import models

class Eleitor(models.Model):
    nome       = models.CharField(max_length=255)
    email      = models.EmailField(unique=True)
    telefone   = models.CharField(max_length=20, blank=True)
    # Outros campos relevantes
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


# eleitores/models.py (ou em um arquivo separado, se preferir)
class MensagemEleitor(models.Model):
    eleitor    = models.ForeignKey(Eleitor, on_delete=models.CASCADE, related_name='mensagens')
    mensagem   = models.TextField()
    enviado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.eleitor.nome} em {self.enviado_em.strftime('%d/%m/%Y')}"
