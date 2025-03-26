from django.contrib import admin
from .models import Eleitor, MensagemEleitor
# Register your models here.
admin.site.register(Eleitor)
admin.site.register(MensagemEleitor)