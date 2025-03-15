import requests
from datetime import datetime
import os

APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_input = input("What did you do for exercise today? ")
# weight_input = int(input("How much do you weight(in KG)? "))
# height_input = int(input("How tall are you?(in cm) "))
# age_input = int(input("How old are you? "))

exercise_stats = {
    "query": user_input
}

response = requests.post(url= nutrition_endpoint,headers=headers, json=exercise_stats)
result = response.json()

sheety_endpoint = os.environ["SHEETY_ENDPOINT"]
sheety_headers = {
    "Authorization": f"Basic {os.environ["SHEETY_HEADER_AUTH"]}"
}
today = datetime.now()
current_time = today.time()

formatted_today = today.strftime("%d/%m/%Y")
formatted_time = current_time.strftime("%H:%M:%S")

for exercise in result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": formatted_today,
            "time": formatted_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    row_response = requests.post(headers=sheety_headers, url=sheety_endpoint, json=sheety_inputs)
    print(row_response.text)