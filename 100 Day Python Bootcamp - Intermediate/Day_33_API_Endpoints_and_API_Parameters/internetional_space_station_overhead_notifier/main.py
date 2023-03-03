import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -40.715820
MY_LONG = 27.094931

# Setting up the email address and password for authentication
my_email = "danielpythoncoding@gmail.com"
password = "fhhkdmfptywewudf"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


# # print(iss_latitude -5, iss_longitude -5)
# print(iss_latitude, iss_longitude)
# print(MY_LAT, MY_LONG)



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
def iss_is_close():
    if iss_longitude -5 <= MY_LONG or iss_longitude +5 <= MY_LONG or iss_longitude <= MY_LONG and iss_latitude -5 <= MY_LAT or iss_latitude +5 <= MY_LAT or iss_latitude <= MY_LAT and time_now >= sunset and time_now <= sunrise:
        send_email()

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="danielbooysenjr@gmail.com",
            msg=f"Subject:ISS Overhead \n\n The ISS is overhead with coor {iss_latitude} and {iss_longitude}"
        )

checking = True

while checking:
    time.sleep(60)
    iss_is_close()

# BONUS: run the code every 60 seconds.



