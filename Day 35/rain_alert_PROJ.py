from requests import get
from twilio.rest import Client

# OpenWeatherMap
API_KEY = '14ded236d6980288e69ac17f359f864a'
MY_LAT = 25.68302095
MY_LNG = 55.77758789062501
EXCLUDE = 'current,minutely,daily,alerts'

# Twilio, outdated credentials, need new ones for this program to work again
ACCOUNT_SID = "AC5a3e9a34971522c147855577c57b7c44"
AUTH_TOKEN = "25ca3e22d3fdb42092cf84a4a50d15c8"
TWILIO_NUMBER = "+18126252507"

# Program runs everyday at 6 AM to notify you if you are meant to bring an umbrella for that day

with get(f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LNG}&exclude={EXCLUDE}&appid={API_KEY}") as response:
    response.raise_for_status()
    hourly_data = [data['weather'][0]['id'] for data in response.json()['hourly'][:12]]  # other information is unneeded

try:
    rain_today = False
    snow_today = False

    for weather in hourly_data:
        if weather < 600:  # raining, snow doesn't count
            rain_today = True
        elif weather < 700:  # snowing
            snow_today = True

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    if rain_today:
        message = client.messages.create(
            body="It will rain today, bring an umbrella!",
            from_=TWILIO_NUMBER,
            to="Enter number here",
        )
    elif snow_today:
        message = client.messages.create(
            body="It will snow today, bring an umbrella, maybe!",
            from_=TWILIO_NUMBER,
            to="Enter number here",
        )
    else:
        message = client.messages.create(
            body="Clear skies today! No umbrella needed!",
            from_=TWILIO_NUMBER,
            to="Enter number here",
        )

    print(message.status)  # check if message is sent or not, expected result is 'queued'
except:
    print("Outdated twilio credentials")