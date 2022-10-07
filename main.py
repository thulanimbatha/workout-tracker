from datetime import datetime
import requests

API_ID = "6381f745"
API_KEY = "2413e64de79f4e39e16c7dda23bf4d20"
NUTRITIONINX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_endpoint = "https://api.sheety.co/f11518c3f269ca4f56dbbd97f5f1f5d8/workoutTracking/workouts"

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

response = requests.post(url=NUTRITIONINX_ENDPOINT, json=parameters, headers=headers)
# response.raise_for_status()
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
    
    sheety_response = requests.post(sheety_endpoint, json=sheet_inputs)
    print(sheety_response.text)
