from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WeatherAlert
from users.models import User
from .forms import WeatherAlertForm 
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = WeatherAlertForm(request.POST, request.FILES)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = user
            alert.save()
            # recipients = UserProfile.objects.filter(receive_alerts=True).values_list('email', flat=True)
            send_mail(
                subject='New Weather Alert',
                message=f'New alert from {alert.user.username} at {alert.location}: {alert.alert_message}',
                from_email='eskury@gmail.com',
                recipient_list=('nicole.inthestars@gmail.com', 'eskury@gmail.com'),
                # from_email=settings.DEFAULT_FROM_EMAIL,
                #  recipient_list=recipients,
#             )
                fail_silently = False
            )
            # print('Email sent to recipients')
            return redirect('profile')
    else:
        form = WeatherAlertForm()
    
    alerts = WeatherAlert.objects.all()
    return render(request, 'alerts/weather_alerts.html', {'user': user,
                                                    'form':form, 'alerts': alerts,
                                                    })

@login_required
def search_alerts(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            results = WeatherAlert.objects.filter(location__icontains=query).order_by('-created_at')
        return render(request, 'alerts/weather_alerts.html', {'alerts': results})
   