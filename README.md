# ShtoshWeatherBot

Telegram bot that can get the current weather from your IP address

![demo](demo.gif)

## Create your own bot

1. Create a new Telegram bot with [BotFather](https://web.telegram.org/k/#@BotFather)

Copy and paste the API token into [config.py](shtosh-weather-bot/config.py)

`BOT_API_TOKEN = 'Paste your API token here'`

2. Create an account on [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)

_Hint: you can use [temporary mail](https://tempail.com/en/) :)_

Сopy and paste the API key into [config.py](shtosh-weather-bot/config.py)

`WEATHER_API = 'Paste your API key here'`

3. Get the latest [Python](https://www.python.org/downloads/) version

4. Create a virtual environment. Not necessary, but highly recommended.

5. Install requirements

`pip install -r requirements.txt`

6. Run [bot.py](shtosh-weather-bot/bot.py)

`python .\shtosh-weather-bot\bot.py`
