import json
import os
from django.conf import settings
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import Forum, Message, Media


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.forum_id = self.scope['url_route']['kwargs']['forum_id']
        self.forum_group_name = f'forum_{self.forum_id}'

        await self.channel_layer.group_add(
            self.forum_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.forum_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        media_url = data.get('media_url', '')
        

        # media = await self.get_media(media_url)
        media = None
        if media_url:
            media = await self.get_or_create_media(media_url)

        forum = await self.get_forum(self.forum_id)
        user = self.scope['user']


        # new_message = await self.create_message(forum, user, message, media)
        new_message = await self.create_message(forum, user, message, media)

        await self.channel_layer.group_send(
            self.forum_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user':  user.username,
                'media_url': media_url
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['user']
        media_url = event.get('media_url', '')

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'media_url': media_url
        }))

    @database_sync_to_async
    def get_or_create_media(self, media_url):
        relative_path = os.path.relpath(media_url, settings.MEDIA_URL)
        # print('Media URL:', media_url)
        media, created = Media.objects.get_or_create(file=relative_path)
        # if created:
        #     print('Media created:', created)
        # else:
        #     print('Media already exists')
        return media
    
    @database_sync_to_async
    def get_forum(self, forum_id):
        return Forum.objects.get(id=forum_id)
    
    @database_sync_to_async
    def create_message(self, forum, user, message, media):
        return Message.objects.create(
            forum=forum,
            sender=user,
            text=message,
            media=media
        )