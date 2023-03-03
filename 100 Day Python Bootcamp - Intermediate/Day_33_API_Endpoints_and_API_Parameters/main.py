import requests

# Using International Space Station API to get current x,y coor of ISS

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]


is_position = (longitude, latitude)
print(is_position)