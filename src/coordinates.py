from dataclasses import dataclass
import aiohttp


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


async def get_coordinates() -> Coordinates:
    """Returns current coordinates using IP address"""
    data = await _get_ip_data()
    latitude, longitude = map(float, data['loc'].split(','))

    return Coordinates(latitude=latitude, longitude=longitude)


async def _get_ip_data() -> dict:
    url = 'http://ipinfo.io/json'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            ip_data = await response.json()
            return ip_data
