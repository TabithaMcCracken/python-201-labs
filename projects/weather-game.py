# Include the current weather into your game mechanics.
# URL = "https://www.metaweather.com/api/"

import requests

city = input(str("What is the closest large city to you?"))

location_URL = f"https://www.metaweather.com/api/location/search/?query={city}"
locaton_id = requests.get(location_URL).json()[0]["woeid"]

weather_url = f"https://www.metaweather.com/api/location/{locaton_id}"
weather_forecast = requests.get(weather_url).json()["consolidated_weather"][0]["weather_state_name"]
print(f"The current weather there is: {weather_forecast}\n")