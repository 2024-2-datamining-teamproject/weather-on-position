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
        #print(data)
        #print(data.get('weather'))
        weather_code = data.get('weather')[0].get('id')
        return weather_code
    else:
        print("Request failed:", response.status_code);

def translate_weather_code(weather_code):
    if weather_code == 800:
        # 맑은 날씨의 경우
        print(0)
        return
    elif weather_code % 100 == 8:
        # 구름 낀 날씨의 경우
        print(1)
        return
    elif weather_code % 100 == 3 or weather_code % 100 == 4:
        # 비오는 날씨의 경우
        print(2)
        return
    elif weather_code % 100 == 6:
        # 눈오는 날씨의 경우
        print(3)
        return
    elif weather_code % 100 == 2 or weather_code == 771 or weather_code == 781:
        # 폭풍치는 날씨의 경우
        print(4)
        return
    elif weather_code % 100 == 7:
        # 안개 낀 날씨의 경우
        print(5)
        return

def main():
    weather_code = get_weather_info(lat, lon)
    translate_weather_code(weather_code)

if __name__ == "__main__":
    main()
