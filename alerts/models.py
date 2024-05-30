from django.db import models
# from django.contrib.auth.models import User
from users.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    receive_alerts = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class UserMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'Message from {self.user.username}: {self.content}'


class WeatherAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    alert_message = models.TextField(max_length=255)
    image = models.ImageField(upload_to='alerts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Weather Alert for {self.user.username}: {self.location}"
