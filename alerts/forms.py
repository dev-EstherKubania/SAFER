from django import forms
from .models import WeatherAlert
from .models import WeatherAlert, UserMessage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class WeatherAlertForm(forms.ModelForm):
    class Meta:
        model = WeatherAlert
        fields = ['location', 'alert_message', 'image']

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['content']
       
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    receive_alerts = forms.BooleanField(required=False, initial=False, label="Receive Alerts")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'receive_alerts')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserProfile.objects.create(user=user, receive_alerts=self.cleaned_data['receive_alerts'])
        return user