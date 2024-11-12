from dotenv import load_dotenv
import os
import requests

# position of Ajou University
lat = 37.280
lon = 127.044

load_dotenv()
API_KEY = os.getenv("API_KEY")

api_url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lon, API_KEY)

def get_weather_info(lat, lon):
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        print(data)

    else:
        print("Request failed:", response.status_code);

def main():
    get_weather_info(lat, lon)
    

if __name__ == "__main__":
    main()
