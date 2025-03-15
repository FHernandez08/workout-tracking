import requests
from datetime import datetime

APP_ID = "84654d16"
API_KEY = "cda65a26976d16b782c5dd87900f9abb"

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

sheety_endpoint = "https://api.sheety.co/31d6797728706171dba074aea445aa54/workoutTracking/workouts"

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

row_response = requests.post(url=sheety_endpoint, json=sheety_inputs)
print(row_response.text)