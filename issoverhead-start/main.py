import requests
from datetime import datetime
from config import send_mail

MY_LAT = 18.520430 # Your latitude
MY_LONG = 73.856743 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
iss_location = {
    "lat": iss_latitude,
    "lng": iss_longitude
}

#Your position is within +5 or -5 degrees of the ISS position.


my_location = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=my_location)
response.raise_for_status()

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position,
# and it is currently dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.

print("---> ISS - ", iss_location)
print("---> MyL -", my_location)


def its_near():
    if iss_location['lat'] - my_location['lat'] in range(-5, 6):
        if iss_location['lng'] - my_location['lng'] in range(-5, 6):
            return True

    return False

if sunset <= time_now.hour <= sunrise:
    if its_near():
        try:
            send_mail()
        except Exception:
            print(Exception.args)
