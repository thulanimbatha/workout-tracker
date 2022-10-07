from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
import requests

API_ID = "6381f745"
API_KEY = "2413e64de79f4e39e16c7dda23bf4d20"
NUTRITIONINX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

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
response.raise_for_status()
data = response.json()
print(data)
