import requests
import datetime
from config import tg_bot_token, open_weather_token, code_to_smile
from aiogram import Bot, types, executor, Dispatcher
import markups as nav


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

def getNowDayWeather(city):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        curTemp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        windSpeed = data["wind"]["speed"]
        sunriseTime = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunsetTime = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenthOfTheDay = sunsetTime - sunriseTime

        weatherDisc = data["weather"][0]["main"]
        if weatherDisc in code_to_smile:
            wd = code_to_smile[weatherDisc]

        return (
              f"{city}\n"
              f"{curTemp}°C {wd}\n\n"
              f"\U0001F4A7 Humidity: {humidity}%\n\U0001F321 Pressure: {pressure} mmHg\n"
              f"\U0001F32C Wind: {windSpeed} m\s\n\U0001F304 Sunrise: {sunriseTime.strftime('%H:%M')}\n"
              f"\U0001F307 Sunset: {sunsetTime.strftime('%H:%M')}\n\U0000231B Daylight hours: {lenthOfTheDay}\n\n"
              f"***Have a nice day!***")

    except:
        return ("\U00002620 Check the name of the city \U00002620 ")



@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,'Hey! Write me the name of the city and I\'ll send you a weather report!'.format(message.from_user),
                           reply_markup=nav.mainMenu)

#@dp.message_handler(commands=["now"])
#async def get_weather(message: types.Message):
#    await bot.send_message(message.from_user.id, getTodayDayWeather(message.text))

@dp.message_handler()
async def get_weather(message: types.Message):
    await bot.send_message(message.from_user.id, getNowDayWeather(message.text))



if __name__ == '__main__':
    executor.start_polling(dp)
