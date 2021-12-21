import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

api_key = ''  #os.environ.get('')
api_end_point = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = ''
auth_token = ''


parameters = {
    "lat": 18.520430,
    "lon": 73.856743,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}


data = requests.get(api_end_point, params=parameters)
data.raise_for_status()

weather_data = data.json()
weather_slice = weather_data['hourly'][:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code)< 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token , http_client=proxy_client)  
    message = client.messages \
                    .create(
                        body="Bring an umbrella",
                        from_='',
                        to=''
                    )

    print(message.status)