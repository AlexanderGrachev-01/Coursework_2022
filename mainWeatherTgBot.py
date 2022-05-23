import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hey! Write me the name of the city and I'll send you a weather report!")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        curWeather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        windSpeed = data["wind"]["speed"]
        sunriseTime = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunsetTime = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenthOfTheDay = sunsetTime - sunriseTime

        await message.reply(
              f"Weather in: {city}\n"
              f"on: {datetime.datetime.now().strftime('%Y.%m.%d  %H:%M')}\n\n"
              f"Temperature: {curWeather}°C\n"
              f"Humidity: {humidity}%\nPressure: {pressure} mmHg\n"
              f"Wind: {windSpeed} m\s\nSunrise: {sunriseTime}\n"
              f"Sunset: {sunsetTime}\nDaylight hours: {lenthOfTheDay}\n\n"
              f"***Have a nice day!***")

    except:
        await message.reply("\U00002620 Check the name of the city \U00002620 ")



if __name__ == '__main__':
    executor.start_polling(dp)
