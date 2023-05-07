import requests
import datetime
from config import tg_bot_token,open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Рад вас видеть! Введите название города: ")


@dp.message_handler()
async def get_weather(message: types.Message):


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
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        temp = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in smiles:
            wd = smiles[weather_description]
        else:
            wd = ""

        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        temp_feels = data["main"]["feels_like"]

        await message.reply(f"***{city}***\n"
              f"Сегодня: {datetime.datetime.now().strftime('%Y-%m-%d')}\n"
              f"cейчас: {datetime.datetime.now().strftime('%H:%M')}\n"
              f"Температура: {temp}C° {wd}\n"
              f"По ощущению: {temp_feels}C°\n"
              f"Влажность: {humidity}%\nВетер: {wind} м/с\n"

              )

    except:
        await message.reply("Проверьте название города")

if __name__ == '__main__':
    executor.start_polling(dp)