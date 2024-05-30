from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from alerts.tasks import send_weather_alert_email_task
from .models import UserProfile, WeatherAlert

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    
@receiver(post_save, sender=WeatherAlert)
def send_weather_alert_email(sender, instance, created, **kwargs):
    if created:
        if instance.user.userprofile.receive_alerts:
            send_weather_alert_email_task.delay(instance.user.id, instance.alert_message)