from typing import Literal, TypeAlias
from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
import aiohttp
import json

from coordinates import Coordinates
import config

Celsius: TypeAlias = float


class WindDirection(IntEnum):
    North = 0
    Northeast = 45
    East = 90
    Southeast = 135
    South = 180
    Southwest = 225
    West = 270
    Northwest = 315


@dataclass(slots=True, frozen=True)
class Weather:
    location: str
    temperature: Celsius
    temperature_feeling: Celsius
    description: str
    wind_speed: float
    wind_direction: str
    sunrise: datetime
    sunset: datetime


async def get_weather(coordinates: Coordinates) -> Weather:
    """Requests the weather in OpenWeather API and returns it"""
    openweather_response = await _get_openweather_response(
        longitude=coordinates.longitude, latitude=coordinates.latitude
    )
    weather = _parse_openweather_response(openweather_response)
    return weather


async def _get_openweather_response(latitude: float, longitude: float) -> str:
    url = config.CURRENT_WEATHER_API_CALL.format(latitude=latitude, longitude=longitude)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_text = await response.text()
            return response_text


def _parse_openweather_response(openweather_response: str) -> Weather:
    openweather_dict = json.loads(openweather_response)
    return Weather(
        location=_parse_location(openweather_dict),
        temperature=_parse_temperature(openweather_dict),
        temperature_feeling=_parse_temperature_feeling(openweather_dict),
        description=_parse_description(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict, 'sunrise'),
        sunset=_parse_sun_time(openweather_dict, 'sunset'),
        wind_speed=_parse_wind_speed(openweather_dict),
        wind_direction=_parse_wind_direction(openweather_dict)
    )


def _parse_location(openweather_dict: dict) -> str:
    return openweather_dict['name']


def _parse_temperature(openweather_dict: dict) -> Celsius:
    return openweather_dict['main']['temp']


def _parse_temperature_feeling(openweather_dict: dict) -> Celsius:
    return openweather_dict['main']['feels_like']


def _parse_description(openweather_dict) -> str:
    return str(openweather_dict['weather'][0]['description']).capitalize()


def _parse_sun_time(openweather_dict: dict, time: Literal["sunrise", "sunset"]) -> datetime:
    return datetime.fromtimestamp(openweather_dict['sys'][time])


def _parse_wind_speed(openweather_dict: dict) -> float:
    return openweather_dict['wind']['speed']


def _parse_wind_direction(openweather_dict: dict) -> str:
    degrees = openweather_dict['wind']['deg']
    degrees = round(degrees / 45) * 45
    if degrees == 360:
        degrees = 0
    return WindDirection(degrees).name
