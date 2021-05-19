import requests

API_KEY = '8793610e7c4019ccd6189b9bc7bad61e'

parameters = {
    "lat": 44.4323,
    "lon": 26.1063,
    "appid": "8793610e7c4019ccd6189b9bc7bad61e",
    "exclude": 'current,minutely,daily'
}

response = requests.get(
    url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

# print(weather_data)
for i in weather_slice:
    condition_code = i["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print('Bring an umbrella')
