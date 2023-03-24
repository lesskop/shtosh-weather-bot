from coordinates import get_coordinates
from api_service import get_weather


async def weather() -> str:
    """Returns a message about the temperature and weather description"""
    wthr = await get_weather(await get_coordinates())
    return f'{wthr.location}, {wthr.description}\n' \
           f'Temperature is {wthr.temperature}°C, feels like {wthr.temperature_feeling}°C'


async def wind() -> str:
    """Returns a message about wind direction and speed"""
    wthr = await get_weather(await get_coordinates())
    return f'{wthr.wind_direction} wind {wthr.wind_speed} m/s'


async def sun_time() -> str:
    """Returns a message about the time of sunrise and sunset"""
    wthr = await get_weather(await get_coordinates())
    return f'Sunrise: {wthr.sunrise.strftime("%H:%M")}\n' \
           f'Sunset: {wthr.sunset.strftime("%H:%M")}\n'
