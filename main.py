# Completed
import requests
from datetime import *
APP_ID = # Your App ID
API_KEY = #Your API_KEY

sheet_endpoint = #this is the api generated output where you want the program to send the data
exercise_input = input("Tell me which exercises you did?")

parameters = {"query": exercise_input,
              "weight_kg": #your weight in KGS,
              "gender": #gender,
              "height_cm": #your height in cms,
              "age": # age
              }
header = {"x-app-id": APP_ID, "x-app-key": API_KEY}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                         json=parameters,
                         headers=header)
result = response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

auth_sheety = # This is app generated auth that sheety api generates

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(#User name))

    print(sheet_response.text)