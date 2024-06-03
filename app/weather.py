import requests
from flask import Blueprint, render_template, url_for, flash, redirect, request
from app.forms import WeatherForm

weather_bp = Blueprint('weather', __name__)

API_KEY = 'your_openweathermap_api_key'

@weather_bp.route('/', methods=['GET', 'POST'])
def index():
    form = WeatherForm()
    weather_data = None
    if form.validate_on_submit():
        city = form.city.data
        weather_data = get_weather(city)
    return render_template('weather/index.html', form=form, weather_data=weather_data)

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
        return weather
    else:
        flash('City not found!', 'danger')
        return None
