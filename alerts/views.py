from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WeatherAlert
from users.models import User
from .forms import WeatherAlertForm 
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

@login_required
def create_weather_alert(request):
    if request.method == 'POST':
        form = WeatherAlertForm(request.POST, request.FILES)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user
            alert.save()
            
            recipients = User.objects.filter(receive_alerts=True).values_list('user__email', flat=True)
            send_mail(
                subject='New Weather Alert',
                message=f'New alert from {alert.user.username} at {alert.location}: {alert.message}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=recipients,
            )
            return redirect('profile')
    else:
        form = WeatherAlertForm()
    return render(request, 'alerts/weather_alerts.html', {'form': form})
