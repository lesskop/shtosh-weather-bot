import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)

CACHE_TIME = 60 * 5  # In seconds