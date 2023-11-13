import requests
import pywhatkit

api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = 'YOUR-API-KEY_HERE'

weather_param = {
    'lat': ADD_LONGITUDE,
    'lon': ADD_LATITUDE,
    'appid': api_key,
}

response = requests.get(url=api_endpoint, params=weather_param)
response.raise_for_status()
weather_data = response.json()['list']

will_rain = False

for i in range(4):
    uid = weather_data[i]['weather'][0]['id']
    if uid < 700:
        will_rain = True

if will_rain:
    pywhatkit.sendwhatmsg_instantly(phone_no='YOUR_Phone_number', message="Take your umbrella!!.\nIt's "
                                                                      "going to rain today")



