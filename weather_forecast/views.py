import datetime
import requests
import os
from django.shortcuts import render
from dotenv import load_dotenv


load_dotenv()

# Create your views here.
def index(request):
    API_KEY = os.getenv('API_KEY')
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    forecast_url = 'https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude=current,minutely,hourly&appid={}'

    if request.method == 'POST':
        city = request.POST['city']

        weather_data, forecast_data, alerts = fetch_weather(city, API_KEY, current_weather_url, forecast_url)

        context = {
            'weather_data': weather_data,
            'forecast_data': forecast_data,
            'alerts': alerts,
        }
        return render(request, 'index.html', context)
    
    return render(request, 'index.html')

# fetch weather data
def fetch_weather(city, api_key, current_weather_url, forecast_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    lon = response['coord']['lon']
    lat = response['coord']['lat']

    forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()

    weather_data = {
        'city': city,
        'country': response['sys']['country'],
        'temperature': round(response['main']['temp'] - 273.15, 1),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'humidity': response['main']['humidity'],
        'wind_speed': response['wind']['speed'],
        'min_temp': round(forecast_response['daily'][0]['temp']['min'] - 273.15, 2),
        'max_temp': round(forecast_response['daily'][0]['temp']['max'] - 273.15, 2),
    }

    forecast_data = []
    for forecast in forecast_response['daily'][1:6]:
        forecast_data.append({
            'day': datetime.datetime.fromtimestamp(forecast['dt']).strftime('%A'),
            'temperature': round(forecast['temp']['day'] - 273.15, 2),
            'description': forecast['weather'][0]['description'],
            'icon': forecast['weather'][0]['icon'],
        })
        
    alerts = []
    if 'alerts' in forecast_response:
        for alert in forecast_response['alerts']:
            alerts.append({
                'event': alert['event'],
                'description': alert['description'],
            })

    return weather_data, forecast_data, alerts
