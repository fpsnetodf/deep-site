from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/agenda/', consumers.AgendaConsumer.as_asgi()),
]
