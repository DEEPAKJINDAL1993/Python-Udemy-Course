import requests
import pandas as pd
import os
from twilio.rest import Client
from config import *

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

MY_LAT = 30.100329
MY_LONG = 75.682019

params = {"lat": MY_LAT,
          "lon": MY_LONG ,
          "cnt":4,
          "units": "metric",
          "lang": "en",
          "appid": ow_api_key}

response = requests.get(OWM_Endpoint, params=params)
response.raise_for_status()
weather_data = response.json()
# print(data)
data = weather_data["list"]

# forecast = [
#     {
#         "date": item["dt_txt"],
#         "forecast": item["weather"][0]["description"]
#     }
#     for item in data
# ]
#
# print(forecast)

weather_codes = [item["weather"][0]["id"] for item in data]
print(weather_codes)

city_name = weather_data["city"]["name"]
df = pd.DataFrame([
    {
        "city": city_name,
        "date": item["dt_txt"],
        "weather_id": item["weather"][0]["id"],
        # "weather_main": item["weather"][0]["main"],
        "forecast": item["weather"][0]["description"],
        "temp": item["main"]["temp"],
        "humidity": item["main"]["humidity"],
        "wind_speed": item["wind"]["speed"]
        # "visibility": item["visibility"]
    }
    for item in data
])
print(df)

will_rain = False
if min(weather_codes) < 700:
    will_rain = True

    client = Client(account_sid, auth_token)

    # message = client.messages.create(
    #     body="It might rain today, remember to bring an ☂️.",
    #     from_="+12164809245",
    #     to="+919815489141",
    # )
    #
    # print(message.status)


    message = client.messages.create(
        body="It might rain today, remember to bring an ☂️.",
        from_='whatsapp:+14155238886',
        to='whatsapp:+919815489141'
    )

    print(message.sid)


# ----------------------------------------------------------------

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ["TWILIO_ACCOUNT_SID"]
# auth_token = os.environ["TWILIO_AUTH_TOKEN"]
