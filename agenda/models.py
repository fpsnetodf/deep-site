# agenda/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

# STATUS_CHOICES = (
#     ('free', 'Livre'),
#     ('pending', 'Pendente'),
#     ('confirmed', 'Confirmada'),
#     ('conflict', 'Conflito'),
# )

# class Agenda(models.Model):
#     title       = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     date        = models.DateTimeField()
#     status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
#     created_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agendas')
#     created_at  = models.DateTimeField(auto_now_add=True)
#     updated_at  = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.title} - {self.date.strftime('%d/%m/%Y %H:%M')}"

# agenda/models.py
# from django.db import models
# from django.conf import settings

STATUS_CHOICES = (
    ('free', 'Livre'),
    ('pending', 'Pendente'),
    ('confirmed', 'Confirmada'),
    ('conflict', 'Conflito'),
)

class Agenda(models.Model):
    title       = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date        = models.DateTimeField()
    status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='agendas')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.date.strftime('%d/%m/%Y %H:%M')}"
