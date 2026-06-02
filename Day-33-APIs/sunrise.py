import requests
from datetime import datetime, timezone
import time

MY_LAT = 30.133801
MY_LONG = 75.807404
# MY_LAT = 20
# MY_LONG = -105

def is_night():
    sunset_url = "https://api.sunrise-sunset.org/json"
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    sunset_response = requests.get(sunset_url, params=parameters)
    data = sunset_response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    now = datetime.now(timezone.utc).hour
    night = now < sunrise or now > sunset
    return night

def iss_location():
    iss_url = "http://api.open-notify.org/iss-now.json"
    iss_response = requests.get(url=iss_url)
    iss_response.raise_for_status()
    iss_latitude = float(iss_response.json()['iss_position']['latitude'])
    iss_longitude = float(iss_response.json()['iss_position']['longitude'])

    in_vicinity = abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5
    return in_vicinity, iss_latitude, iss_longitude

while True:
    in_vicinity, iss_latitude, iss_longitude = iss_location()
    night = is_night()

    if in_vicinity:
        if is_night:
            print(f"ISS may be overhead. It's a night! Currently at Lat: {iss_latitude} and Long: {iss_longitude}.")
        else:
            print(f"ISS may be overhead. But it's daytime. Currently at Lat: {iss_latitude} and Long: {iss_longitude}.")
    else:
        if is_night:
            print(f"ISS may be far off. But it's night out there. Currently at Lat: {iss_latitude} and Long: {iss_longitude}.")
        else:
            print(f"ISS may be far off. Also it's day out there. Currently at Lat: {iss_latitude} and Long: {iss_longitude}.")

    time.sleep(30)