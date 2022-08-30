FROM python:3.9-slim-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
COPY . .
RUN pip3 install -r requirements.txt

# Run the application:
COPY ip-weather-bot/bot.py .
CMD ["python", "bot.py"]
