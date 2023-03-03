# # # Workout Tracking Using Google Sheets # # #
import requests
from datetime import datetime

APP_KEY = "f991d766e9369d48553b46169e35d47a"
APP_ID = "9e42d57d"
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
TOKEN = "kjngfkjadklgjanklgnadjg"

daily_exercises = input("Tell me what exercises you did today: ")

HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content_Type": "json",
    "Authorization": TOKEN
}

params = {
    "query": daily_exercises,
}

response = requests.post(url=ENDPOINT, json=params, headers=HEADER)
response.raise_for_status()
data = response.json()

excercise_name = data["exercises"][0]["user_input"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]
now = datetime.now()
current_date = now.strftime("%m/%d/%Y")
time = datetime.time(now)
current_time = time.strftime("%H:%M:%S")



# # # Creating a new row

USERNAME = "9d9f8c50d70de27a6f640887fe69ccef"
PROJECT_NAME = "tracking"
SHEET_NAME = "tracker"

SHEETY_ENDPOINT = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
body = {
    "tracker": {
        "date": current_date,
        "time": current_time,
        "exercise": excercise_name,
        "duration": duration,
        "calories": calories
    }
}

training_information = requests.post(url=SHEETY_ENDPOINT, json=body, headers=HEADER)
training_information.raise_for_status()
training_information.json()
