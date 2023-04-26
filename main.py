import requests
import os
from twilio.rest import Client

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "67d85adf61f82d1fdf8b9c7d84291d92"
account_sid = 'AC279114eb002d447ce1d80408b2bf36a3'
auth_token = 'f890bdd1cfecd6bb4944aa8c1cdb5e7f'

weather_params = {
    "lat": 50.064651,
    "lon": 19.944981,
    "appid": api_key,
}

request = requests.get(OWM_Endpoint, params=weather_params)
list = request.json()["list"]
sliced_list = list[:12]
condition = [item["weather"][0]["id"] for item in sliced_list]



will_rain = False

for item in condition:
    if int(item) <700:
        will_rain = True


if will_rain:
    print("Bring an umbrella.")

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_='+18',
    to='+48'
    )

print(message.sid)

