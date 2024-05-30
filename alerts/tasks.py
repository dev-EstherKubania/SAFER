from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

@shared_task
def send_weather_alert_email_task(user_id, alert_message):
    user = User.objects.get(id=user_id)
    subject = 'Weather Alert'
    message = alert_message
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
