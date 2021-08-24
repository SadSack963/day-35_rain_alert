# OpenWeatherMap
# https://github.com/SadSack963/day-35_rain_alert.git

import requests
import json
import send_sms
import winsound
from urllib.request import urlretrieve

import os
from dotenv import load_dotenv


def talk(message):
    # Thanks to Alieksiei for this idea
    # https://www.udemy.com/course/100-days-of-code/learn/#questions/15686144

    # http://voicerss.org/api/
    TTS_URL = "https://api.voicerss.org/"
    params = {
        'key': TTS_api_key,
        'src': message,
        'hl': 'en-gb',
        'v': 'Nancy',  # Voices for en-gb: Alice (default), Nancy, Lily, Harry
        'c': 'WAV'  # Codec: MP3, WAV (default), AAC, AGG, CAF
    }
    response = requests.get(TTS_URL, params=params)
    response.raise_for_status()
    urlretrieve(response.url, "speech.wav")
    winsound.PlaySound("speech.wav", winsound.SND_NODEFAULT)


load_dotenv("E:/Python/EnvironmentVariables/.env")
TTS_api_key = os.getenv("TTS_API_Key")
OWM_api_key = os.getenv("APIKey-OpenWeatherMap-Python")
city_name = "Milton Keynes"
lon = -0.7558
lat = 52.0417

current_url = "https://api.openweathermap.org/data/2.5/weather"
current_parameters = {
    "q": city_name,
    "units": "metric",
    "appid": OWM_api_key
}

response = requests.get(url=current_url, params=current_parameters, timeout=1)
response.raise_for_status()

data = response.json()
print(f'current {data = }')


one_call_url = "https://api.openweathermap.org/data/2.5/onecall"
one_call_parameters = {
    "lat": lat,
    "lon": lon,
    "exclude": "current,minutely,daily",
    "units": "metric",
    "appid": OWM_api_key
}

response = requests.get(url=one_call_url, params=one_call_parameters, timeout=1)
response.raise_for_status()

data = response.json()
print(f'one_call {data = }')

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
            talk(message)
            # send_sms.send_sms(message)
            break
