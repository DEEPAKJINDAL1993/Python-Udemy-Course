from config import app_id,app_key,gsheet_endpoint,gsheet_bearer_token
import requests
from datetime import datetime
import gspread
import google.auth
import pandas as pd

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

# --------------------------------------

gc = gspread.service_account(
    filename="../my-workouts-498507-51ccaf20fb1a.json"
)
print(gc)

sheet = gc.open("My Workouts").worksheet("workouts")
print(sheet)

# dataframe = pd.DataFrame(sheet.get_all_records())
# print(dataframe)

# Post new rows in GSheet
workout_body = {
        "Date": datetime.now().strftime("%d/%m/%Y"),
        "Time": datetime.now().strftime("%X"),
        "Exercise": workout_data["exercises"][0]["name"].title(),
        "Duration": workout_data["exercises"][0]["duration_min"],
        "Calories": workout_data["exercises"][0]["nf_calories"]
}

sheet.append_row([
    workout_body["Date"],
    workout_body["Time"],
    workout_body["Exercise"],
    workout_body["Duration"],
    workout_body["Calories"]
    ]
)

