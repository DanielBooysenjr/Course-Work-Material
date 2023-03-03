# # # Detect if it will rain in the next 12 hours, if it does, it will send you an SMS # # #

import requests

API = "e6f48c3bc92d41ea811105335232602"

parameters = {
    "key": API,
    "q": "potchefstroom",
    "aqi": "no",
    "tp": 15
}


response = requests.get("http://api.weatherapi.com/v1/forecast.json", params = parameters)
response.raise_for_status()
data = response.json()

will_rain = False

forecast_slice = data["forecast"]["forecastday"][0]["hour"][:12]

for hour_data in forecast_slice:
    condition_code = hour_data["condition"]["code"]
    if condition_code > 1063:
        will_rain = True

if will_rain:
    print("Bring an umbrella")