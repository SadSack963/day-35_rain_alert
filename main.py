# OpenWeatherMap
# https://github.com/SadSack963/day-35_rain_alert.git

import os
import requests
import json
import send_sms

api_key = os.environ.get("APIKey-OpenWeatherMap-Python")
city_name = "Milton Keynes"
lon = -0.7558
lat = 52.0417

current_url = "https://api.openweathermap.org/data/2.5/weather"
current_parameters = {
    "q": city_name,
    "units": "metric",
    "appid": api_key
}

one_call_url = "https://api.openweathermap.org/data/2.5/onecall"
one_call_parameters = {
    "lat": lat,
    "lon": lon,
    "exclude": "current,minutely,daily",
    "units": "metric",
    "appid": api_key
}

response = requests.get(url=one_call_url, params=one_call_parameters, timeout=1)
response.raise_for_status()

data = response.json()
print(data)

with open("./data/one_call_data.json", mode="w") as file:
    json.dump(data, fp=file)

with open("./data/one_call_data.json", mode="r") as file:
    data = json.load(fp=file)

# print(data["hourly"][0]["weather"][0]["id"])

# Get data for the first 12 hours
data_slice = data["hourly"][:12]
# Check all hours for weather id < 700 (precipitation)
for hour in data_slice:
    for weather in hour["weather"]:
        if weather["id"] < 700:
            message = f"{weather['description']} - Take an umbrella"
            print(message)
            # send_sms.send_sms(message)
            break
