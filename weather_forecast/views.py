import datetime
import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

# fetch weather data
def fetch_weather(city, api_key, current_weather_url, forecast_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    lon = response['coord']['lon']
    lat = response['coord']['lat']

    forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

    forecast_data = []
    for forecast in forecast_response['daily']:
        forecast_data.append({
            'day': datetime.datetime.fromtimestamp(forecast['dt']).strftime('%A'),
            'temperature': round(forecast['temp']['day'] - 273.15, 2),
            'description': forecast['weather'][0]['description'],
            'icon': forecast['weather'][0]['icon'],
        })

    alerts = []
    for alert in forecast_response['alerts']:
        alerts.append({
            'event': alert['event'],
            'description': alert['description'],
        })

    return weather_data, forecast_data, alerts
