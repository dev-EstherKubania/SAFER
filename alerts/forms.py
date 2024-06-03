from .models import WeatherAlert
from django import forms

class WeatherAlertForm(forms.ModelForm):
    class Meta:
        model = WeatherAlert
        fields = ['location', 'alert_message', 'image']
