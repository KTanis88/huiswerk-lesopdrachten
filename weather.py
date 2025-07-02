import requests

# city_name = "Nijmegen"
# api_key = "dae7a1216c2f4af222bd7e3b41842b4c"

def get_weather_data(city_name, api_key) :
    url = (f"http://api.openweathermap.org/data/2.5/weather")
    params = {"q" : city_name,
          "appid" : api_key}

    response = requests.get(url, params)

    if response.ok:
        return response.json()
    else:
        print("Er is iets misgegaan.")

def display_weather_info(weather_data):
    city= weather_data["name"]
    temp = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    print(f"Het weer in {city}: ")
    print(f"Temperatuur : {temp} F")
    print(f"Beschrijving : {description.capitalize()}")
    print(f"Luchtvochtigheid : {humidity}% ")
    print(f"Wind snelheid : {wind_speed} m/s ")

def main() :
    city_name = input("Voer je stad in: ").strip().lower()

    while not city_name:
        print("Stadsnaam kan niet leeg zijn! ")
        city_name = input("Voer je stad in: ").strip().lower()

    api_key = "dae7a1216c2f4af222bd7e3b41842b4c"
    data = get_weather_data(city_name, api_key)

    display_weather_info(data)

main()