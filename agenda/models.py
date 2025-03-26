# agenda/models.py
from django.db import models
from campanha.models import Coordenador  # se houver relacionamento, ou remova se não necessário

class Agenda(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('pendente', 'Pendente'),
            ('confirmada', 'Confirmada'),
            ('conflitante', 'Conflitante')
        ]
    )
    # Se quiser incluir um campo de relacionamento com Coordinador, descomente:
    coordenador = models.ForeignKey(Coordenador, on_delete=models.CASCADE, related_name="agendas")

    def __str__(self):
        return f"{self.title} - {self.date}"

