# ShtoshWeatherBot

Telegram bot that can get the current weather from your IP address

![demo](demo.gif)

## Getting started

1. Clone this repository to your local machine:

`git clone https://github.com/lesskop/shtosh-weather-bot.git`

2. Install Python 3.10+ version

3. Create a virtual environment. Not necessary, but highly recommended.

4. Install requirements:

`pip install -r requirements.txt`

5. Create an `.env` file in the root of your project directory and add your Telegram bot API token:

`BOT_API_TOKEN=bot-token-here`

6. Create an account on [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)

*Hint: you can use [temporary mail](https://tempail.com/en/) :)*

Сopy and paste the API key into `.env` file

`WEATHER_API=api-key-here`

7. Run [bot.py](shtosh-weather-bot/bot.py) from project directory:

`python .\shtosh-weather-bot\bot.py`

## Usage

This Telegram bot supports the following commands:

* `/start` - Start the bot and get a welcome message with the weather at your location.
* `/help` - Display the available commands.
* `/weather` - Display the weather.
* `/wind` - Display wind speed and direction.
* `/sun_time` - Display sunrise and sunset times.

## License

This Telegram bot is open source and available under the [MIT License](LICENCE).

---
[YouTube video](https://youtu.be/9cOnJLpwbpU)

[Статья на Хабре](https://habr.com/p/684038/)