# Habit Tracker Using Pixela API

import requests
from datetime import datetime

USERNAME = "danielbooysen"
TOKEN = "KLJDKJI)@#J@LMS"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=parameters)
# print(response.text)

# GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "Min",
#     "type": "int",
#     "color": "sora",
# }

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"

today = datetime.now()
# today_strftime = (today.strftime("%Y%m%d"))

body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you program today? "),
}

response = requests.post(url=PIXEL_ENDPOINT, json=body, headers=headers)
print(response.text)

update_pixel = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"


# response = requests.delete(url=update_pixel, headers=headers)
# print(response.text)