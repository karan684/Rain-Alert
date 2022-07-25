import requests
from twilio.rest import Client


api_key = "59c5db87cf2e92a053f51497c3f7a4ba"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC5afb58b23ecfcc9ad79951f6ab9dcea2"
auth_token = "42d51494924435e5f72aaf4e257b5439"

MY_LAT = 16.704987
MY_LONG = 74.243256
exclude = "current,minutely,daily,alerts"
count = 0
parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : api_key,
    "exclude" : exclude
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()

for i in range(0, 12):
    if weather_data["hourly"][i]["weather"][0]["id"] < 700:
        count += 1

if count > 0 :
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂",
        from_="+14025425341",
        to=" " #put ur phone number there
    )
    print(message.status)
