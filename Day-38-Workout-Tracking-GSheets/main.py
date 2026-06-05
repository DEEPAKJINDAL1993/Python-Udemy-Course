from config import app_id,app_key,gsheet_endpoint,gsheet_bearer_token
import requests
from datetime import datetime
import gspread
import google.auth

BASE_URL = 'https://app.100daysofpython.dev'

ENDPOINT_URL = f"{BASE_URL}/v1/nutrition/natural/exercise"

headers = {
    "x-app-id": app_id,
    "x-app-key": app_key
}

WEIGHT_KG = 84
HEIGHT_CM = 175
AGE = 32
GENDER = 'male'

user_input = input("Tell me which exercise you did.\t")

request_body_params = {
    "query": user_input,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER
}

response = requests.post(url=ENDPOINT_URL, json=request_body_params, headers=headers)
response.raise_for_status()
workout_data = response.json()
print(workout_data)


# Post new rows in GSheet
workout_body = {
    "workout": {
        "date": datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%X"),
        "exercise": workout_data["exercises"][0]["name"].title(),
        "duration": workout_data["exercises"][0]["duration_min"],
        "calories": workout_data["exercises"][0]["nf_calories"]
    }
}

auth_header = {
    "Authorization": f"Bearer {gsheet_bearer_token}",
}

gsheet_post_response = requests.post(url=gsheet_endpoint, json=workout_body, headers=auth_header)
gsheet_post_response.raise_for_status()
print(gsheet_post_response.text)

# Get all records from GSheet
gsheet_get_response = requests.get(gsheet_endpoint, headers=auth_header)
gsheet_get_response.raise_for_status()
print(gsheet_get_response.text)

