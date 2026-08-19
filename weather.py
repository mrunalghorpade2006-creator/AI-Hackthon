import requests

def get_weather(city):

    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

    response = requests.get(url)
    data = response.json()

    if "results" not in data:
        return "City not found"

    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m"
    )

    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    temperature = weather_data["current"]["temperature_2m"]
    wind_speed = weather_data["current"]["wind_speed_10m"]

    return f"{city}: {temperature}°C, Wind Speed: {wind_speed} km/h"


print(get_weather("Mumbai"))