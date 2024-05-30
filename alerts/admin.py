from django.contrib import admin
from .models import UserProfile, WeatherAlert

admin.site.register(UserProfile)
admin.site.register(WeatherAlert)
