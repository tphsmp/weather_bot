import requests
from datetime import datetime
from functions import wind_direction
from config import bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Нужен прогноз погоды? Просто напиши мне название города")


@dp.message_handler()
async def get_weather(message: types.Message):

        code_to_smile = {
            "Clear": " \U00002600",
            "Clouds": " \U00002601",
            "Rain": " \U00002614",
            "Drizzle": " \U00002614",
            "Thunderstorm": " \U000026A1",
            "Snow": " \U0001F328",
            "Mist": " \U0001F32B"
        }

        try:
            r = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric&lang=RU")
            data = r.json()

            city = data["name"]
            cur_weather = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            sunrise_timestamp = datetime.time(datetime.fromtimestamp(data["sys"]["sunrise"]))
            sunset_timestamp = datetime.time(datetime.fromtimestamp(data["sys"]["sunset"]))
            wind_dir = wind_direction(int(data["wind"]["deg"]))
            wind_spd = data["wind"]["speed"]
            weather_conditions = data["weather"][0]["main"]
            weather_conditions2 = data["weather"][0]["description"]

            if weather_conditions in code_to_smile:
                wd = code_to_smile[weather_conditions]
            else:
                wd = "Лучше сами посмотрите"

            day_length = datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.fromtimestamp(data["sys"]["sunrise"])

            await message.reply(
                f"Погода в: {city} на {datetime.now().strftime('%d-%m-%Y %H:%M')}\n "
                f"Температура: {cur_weather} С {weather_conditions2} {wd} \n "
                f"Влажность: {humidity}%\n "
                f"Атмосферное давление: {pressure} мм.рт.ст\n "
                f"Ветер: {wind_dir} {wind_spd} м/с\n "
                f"Восход: {sunrise_timestamp}\n "
                f"Закат {sunset_timestamp}\n "
                f"Продолжительность светового дня: {day_length}")


        except:
            await message.reply(" \U00002620 Проверьте название города \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)
