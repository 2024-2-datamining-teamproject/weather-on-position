from dotenv import load_dotenv
import os
import requests

# position of Ajou University
lat = 37.280
lon = 127.044

load_dotenv()
API_KEY = os.getenv("API_KEY")

api_url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lon, API_KEY)

genre_dic = {
        0:["Adventure", "Animation", "Children", "Comedy", "Musical"],
        1:["Drama", "Romance", "Fantasy", "Mystery"],
        2:["Romance", "Drama", "Crime", "Film-Noir"],
        3:["Fantasy", "Romance", "Adventure", "IMAX"],
        4:["Action", "Thriller", "Horror", "Sci-Fi"],
        5:["Mystery", "Horror", "Film-Noir", "Western"]
        }


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
        return 0
    elif weather_code // 100 == 8:
        # 구름 낀 날씨의 경우
        return 1
    elif weather_code // 100 == 3 or weather_code // 100 == 4:
        # 비오는 날씨의 경우
        return 2
    elif weather_code // 100 == 6:
        # 눈오는 날씨의 경우
        return 3
    elif weather_code // 100 == 2 or weather_code == 771 or weather_code == 781:
        # 폭풍치는 날씨의 경우
        return 4
    elif weather_code // 100 == 7:
        # 안개 낀 날씨의 경우
        return 5

def main():
    weather_code = get_weather_info(lat, lon)
    print(weather_code)
    translated_weather_code = translate_weather_code(weather_code)
    print(translated_weather_code)
    print(genre_dic.get(translated_weather_code))

if __name__ == "__main__":
    main()
