import requests
import os
from lexicon import LEXICON as L

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

APITOKEN = os.getenv('APITOKEN')

URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}&lang=ru'

async def get_weather_to_city(city: str):
    try:
        responce = requests.get(URL.format(city, APITOKEN))
    except:
        return L['server_unavaiable']
    if responce.status_code == 200:
        responce = responce.json()
        desc = responce['weather'][0]['description']
        temp = responce['main']['temp']
        feels_temp = responce['main']['feels_like']
        humidity = responce['main']['humidity']
        speed_wind = responce['wind']['speed']
        return L['weather_message'].format(city, desc, temp, feels_temp, humidity, speed_wind)
    else:
        if responce.json()['message'] == 'city not found':
            return L['city_not_found']
        else:
            return L['server_unavaiable']