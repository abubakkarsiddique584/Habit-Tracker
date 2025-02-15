from _datetime import datetime

import requests
APP_ID = "Your Sheety Api Id"
API_KEY = "Your sheety Api Key"
sheet_endpoint ="Your Sheety Endpoint"

GENDER = "Male"
WEIGHT_KG = 78
HEIGHT_CM = 167
AGE = 23
USERNAME = "abubakar"#Your Sheety Username
PASSWORD = "Your password"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

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

    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


    # #Basic Authentication
    # sheet_response = requests.post(
    #   sheet_endpoint,
    #   json=sheet_inputs,
    #   auth=(
    #       USERNAME,
    #       PASSWORD,
    #   )
    # )
    # print(sheet_response.text)

    #Bearer Token Authentication
    bearer_headers = {
    "Authorization": "Your Token Header"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )
print(sheet_response.text)
