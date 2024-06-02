from django.contrib import admin

from .models import Region, Forum, Message, Media

# Register your models here.
admin.site.register(Region)
admin.site.register(Forum)
admin.site.register(Media)
admin.site.register(Message)