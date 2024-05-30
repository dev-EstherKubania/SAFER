from django.urls import path
from .views import create_weather_alert, user_alerts
from .views import signup
from . import views
from .views import create_weather_alert, user_alerts, home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', home, name='home'),
    path('create/', create_weather_alert, name='create_weather_alert'),
    path('alerts/', user_alerts, name='user_alerts'),
    path('signup/', signup, name='signup'),
     path('profile/', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
