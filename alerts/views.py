from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WeatherAlert, UserProfile, UserMessage
from .forms import WeatherAlertForm, UserMessageForm
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

from django.conf import settings

@login_required
def create_weather_alert(request):
    if request.method == 'POST':
        form = WeatherAlertForm(request.POST, request.FILES)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user
            alert.save()
            
            recipients = UserProfile.objects.filter(receive_alerts=True).values_list('user__email', flat=True)
            send_mail(
                subject='New Weather Alert',
                message=f'New alert from {alert.user.username} at {alert.location}: {alert.message}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=recipients,
            )
            return redirect('profile')
    else:
        form = WeatherAlertForm()
    return render(request, 'create_weather_alert.html', {'form': form})

@login_required
def user_alerts(request):
    alerts = WeatherAlert.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'user_alerts.html', {'alerts': alerts})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'alerts/profile.html')

def profile(request):
    user = request.user
    if request.method == 'POST':
        form = WeatherAlertForm(request.POST, request.FILES)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = user
            alert.save()
            return redirect('profile')
    else:
        form = WeatherAlertForm()
    
    alerts = WeatherAlert.objects.all()
    return render(request, 'alerts/profile.html', {'user': user,
        'form':form, 'alerts': alerts,
        })
