import requests
from dotenv import load_dotenv
from pprint import pprint
import os

load_dotenv()


def get_current_weather(city="Lahore"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    city = input("City Name: ")

    # check to see if the input is empty, and setting a default value. Any city default value can be set here as well.
    if not bool(city.strip()):
        city = "Gujranwala"

    weather_data = get_current_weather(city)
    pprint(weather_data)