from channels.generic.websocket import WebsocketConsumer
import json

class AgendaConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'message': 'Conexão estabelecida com WebSocket'
        }))

    def receive(self, text_data):
        data = json.loads(text_data)
        self.send(text_data=json.dumps({
            'message': f"Notificação recebida: {data['content']}"
        }))
