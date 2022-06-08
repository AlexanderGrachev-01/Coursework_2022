import requests
import datetime
from config import open_weather_token, code_to_smile

def getNowWeather(city):  # Weather at the moment
    try:
        print(city)
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        print(data)

        city = data["name"]
        curTemp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        windSpeed = data["wind"]["speed"]

        weatherDisc = data["weather"][0]["main"]
        if weatherDisc in code_to_smile:
            wd = code_to_smile[weatherDisc]

        return (
              f"{city}\n"
              f"{curTemp}°C {wd}\n\n"
              f"\U0001F4A7 Humidity: {humidity}%\n"
              f"\U0001F321 Pressure: {pressure} mmHg\n"
              f"\U0001F32C Wind: {windSpeed} m\s\n\n"
              f"***Have a nice day!***")

    except:
        return ("\U00002620 Check the name of the city \U00002620 ")


def getDayWeather(city):  # Weather for Today
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        print(data)

        city = data["name"]
        curTemp = data["main"]["temp"]
        feelsTemp = data["main"]["feels_like"]
        maxTemp = data["main"]["temp_max"]
        minTemp = data["main"]["temp_min"]
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
              f"*Today "
              f"({datetime.datetime.now().strftime('%Y-%m-%d')})*\n\n"
              f"{city}\n{curTemp}°C  {wd}\n"
              f"Feels like: {feelsTemp}\n\n"
              f"**Min / Max**\n"
              f"{minTemp} / {maxTemp}\n\n"
              f"\U0001F4A7 Humidity: {humidity}%\n\U0001F321 Pressure: {pressure} mmHg\n"
              f"\U0001F32C Wind: {windSpeed} m\s\n\U0001F304 Sunrise: {sunriseTime.strftime('%H:%M')}\n"
              f"\U0001F307 Sunset: {sunsetTime.strftime('%H:%M')}\n\U0000231B Daylight hours: {lenthOfTheDay}\n\n"
              f"***Have a nice day!***")

    except:
        return ("\U00002620 Check the name of the city \U00002620 ")


def getTomorrowWeather(city):  # Weather for Tomorrow
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        print(data)

        date = datetime.datetime.today()
        date += datetime.timedelta(days=1)
        city = data["name"]
        curTemp = data["main"]["temp"]
        feelsTemp = ""
        maxTemp = ""
        minTemp = ""
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
              f"*Tomorrow "
              f"({date.strftime('%Y-%m-%d')})*\n\n"
              f"{city}\n{curTemp}°C  {wd}\n"
              f"Feels like: {feelsTemp}\n\n"
              f"**Min / Max**\n"
              f"{minTemp} / {maxTemp}\n\n"
              f"\U0001F4A7 Humidity: {humidity}%\n\U0001F321 Pressure: {pressure} mmHg\n"
              f"\U0001F32C Wind: {windSpeed} m\s\n\U0001F304 Sunrise: {sunriseTime.strftime('%H:%M')}\n"
              f"\U0001F307 Sunset: {sunsetTime.strftime('%H:%M')}\n\U0000231B Daylight hours: {lenthOfTheDay}\n\n"
              f"***Have a nice day!***")

    except:
        return ("\U00002620 Check the name of the city \U00002620 ")


def getFiveDayWeather(city):  # Weather for 5 days
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        print(data)

        city = ""
        maxTemp1 = ""
        minTemp1 = ""
        weatherDisc1 = ""
                #if weatherDisc1 in code_to_smile:
        wd1 = ""
        maxTemp2 = ""
        minTemp2 = ""
        weatherDisc2 = ""
                #if weatherDisc2 in code_to_smile:
        wd2 = ""
        maxTemp3 = ""
        minTemp3 = ""
        weatherDisc3 = ""
                #if weatherDisc3 in code_to_smile:
        wd3 = ""
        maxTemp4 = ""
        minTemp4 = ""
        weatherDisc4 = ""
                #if weatherDisc4 in code_to_smile:
        wd4 = ""
        maxTemp5 = ""
        minTemp5 = ""
        weatherDisc5 = ""
                #if weatherDisc5 in code_to_smile:
        wd5 = ""

        return (
              f"{city}\n\n"
              f"Today {wd1}\n"
              f"{minTemp1}°C / {maxTemp1}°C\n\n"
              f"Tomorrow {wd2}\n"
              f"{minTemp2}°C / {maxTemp2}°C\n\n"
              f" {wd3}\n"
              f"{minTemp3}°C / {maxTemp3}°C\n\n"
              f" {wd4}\n"
              f"{minTemp4}°C / {maxTemp4}°C\n\n"
              f" {wd5}\n"
              f"{minTemp5}°C / {maxTemp5}°C\n\n"
              f"***Have a nice day!***")

    except:
        return ("\U00002620 Check the name of the city \U00002620 ")