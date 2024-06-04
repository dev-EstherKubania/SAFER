from django.db import models
from users.models import User

   
class WeatherAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    alert_message = models.TextField(max_length=255)
    image = models.ImageField(upload_to='alerts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Weather Alert for {self.user.username}: {self.location}"
    