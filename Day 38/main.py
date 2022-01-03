import requests
from datetime import datetime

GENDER = 'Male'
WEIGHT_KG  = 65
HEIGHT_CM = 170
AGE = 21
APP_ID = '229fa926'
API_KEY = 'b08f594c770dfebbef08731879a86028'

exercise_endpoint  = 'NUTRITONIX_ENDPOINT'
sheet_endpoint = 'SHEETY_ENDPOINT'

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

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)




#Bearer Token Authentication
bearer_headers = {
"Authorization": "Bearer YOUR_TOKEN"
}
sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs, 
    headers=bearer_headers
)