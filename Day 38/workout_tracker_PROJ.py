from requests import get, post
from datetime import datetime as dt

APP_KEY = "af0db86659b67587ac2801ad9fd0da04"
APP_ID = "95d9a2f8"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0",  # development mode
}

SHEETY_HEADERS = {
    "Authorization": "Bearer hgfiuyrqegfiowgfiq3g438o7qitgf3qhf3iquwefg3of",
}

exercises_done = input("Enter exercises done: ")

workout_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

workout_params = {
    "query":exercises_done,
    "gender": "male",
    "weight_kg": 68,
    "height_cm": 175,
    "age": 19,
}

with post(url=workout_endpoint, json=workout_params, headers=HEADERS) as response:
    data = response.json()

SHEETY_ENDPOINT = "https://api.sheety.co/e05cec963399e42a3b96c83cde4dd2b4/myWorkouts/workouts"

for exercise in data['exercises']:
    exercise_params = {
        "workout": {
            "date": dt.now().strftime("%d/%m/%Y"),
            "time": dt.now().strftime("%H:%M:%S"),
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }

    with post(url=SHEETY_ENDPOINT, json=exercise_params, headers=SHEETY_HEADERS) as response:
        print(response.text)
