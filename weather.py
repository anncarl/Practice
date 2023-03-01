#get data from openweather API

import requests
import json 

api_key = "get API key from openweather.org"
base_url= "https://api.openweathermap.org/data/2.5/weather"
parameters = {
    "q":"Nairobi",
    "appid": api_key,
}
weather = requests.get(base_url,params=parameters)

# weather = weather.json()

#print(type(weather.text))

#using the json package
#dict = json.loads(weather.text)
weather = weather.json() 

print(weather["weather"][0]["description"])