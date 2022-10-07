from datetime import datetime
import requests
import os

API_ID = os.environ.get("workouttrackerAPI_ID")
API_KEY = os.environ.get("workouttrackerAPI_KEY")
NUTRITIONINX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
TOKEN = os.environ.get("SHEETY_TOKEN")

parameters = {
    "query"     : input("Exercises done: "),
    "gender"    : "male",
    "weight_kg" : 79,
    "height_cm" : 178,
    "age"       : 26,
}

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

sheety_headers = {
    "Authorization" : TOKEN
}

response = requests.post(url=NUTRITIONINX_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()
# print(data)

todays_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date" : todays_date,
            "time" : time_now,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }
    
    sheety_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_headers)
    print(sheety_response.text)
