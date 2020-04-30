import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChillConsumer(WebsocketConsumer):
    def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'room_%s' % self.room_id
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        message = text_data_json['message']
        user = text_data_json['user']['name']
        if action == 'game':
            pass
        elif action == 'chat-message':
            message = self.handle_chat_message(message, user)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'comment_message',
                'action': action,
                'message': message,
                'user': user,
            }
        )

    def comment_message(self, event):
        self.send(text_data=json.dumps(event))

    @staticmethod
    def handle_chat_message(message, user):
        return f'{user}: {message}'
