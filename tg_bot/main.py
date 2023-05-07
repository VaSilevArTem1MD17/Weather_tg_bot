import datetime

import requests
from pprint import pprint
from config import open_weather_token

def get_weather(city,open_weather_token):


    smiles = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }


    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data=r.json()
        #pprint(data)

        city=data["name"]
        temp=data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in smiles:
            wd = smiles[weather_description]
        else:
            wd = ""

        humidity=data["main"]["humidity"]
        wind=data["wind"]["speed"]
        temp_feels=data["main"]["feels_like"]

        print(f"***{city}***\n"
            f"Сегодня: {datetime.datetime.now().strftime('%Y-%m-%d')}\n"
              f"cейчас: {datetime.datetime.now().strftime('%H:%M')}\n"
              f"Температура: {temp}C° {wd}\n"
              f"По ощущению: {temp_feels}C°\n"
              f"Влажность: {humidity}%\nВетер: {wind} м/с\n"


              )

    except Exception as ex:
        print(ex)
        print("Проверьте название города")

def main():
    city=input("введите город: ")
    get_weather(city,open_weather_token)

if __name__ == '__main__':
    main()