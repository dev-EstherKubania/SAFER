from django.urls import path
from .import views

urlpatterns=[
    # path('', views.create_weather_alert, name='create_alert')
    path('', views.profile, name='profile'),
    path('search/', views.search_alerts, name='search_alerts'),
] 