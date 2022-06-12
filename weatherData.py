import requests
import datetime
from config import open_weather_token, code_to_smile

def getData(city, td):
    print(city)
    if td == True:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
    else:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={open_weather_token}&units=metric"
        )
    data = r.json()
    print(data)
    return data



def getNowWeather(city):  # Weather at the moment
    try:
        data = getData(city, True)

        city = data["name"]
        curTemp = '{0:+3.0f}'.format(data["main"]["temp"])
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
        data = getData(city, True)

        city = data["name"]
        curTemp = '{0:+3.0f}'.format(data["main"]["temp"])
        feelsTemp = '{0:+3.0f}'.format(data["main"]["feels_like"])
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        windSpeed = data["wind"]["speed"]
        sunriseTime = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunsetTime = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenthOfTheDay = sunsetTime - sunriseTime

        weatherDisc = data["weather"][0]["main"]
        if weatherDisc in code_to_smile:
            wd = code_to_smile[weatherDisc]

        data = getData(city, False)
        maxTemp = '{0:+3.0f}'.format(data["list"][0]["main"]["temp_max"])
        minTemp = '{0:+3.0f}'.format(data["list"][0]["main"]["temp_min"])

        return (
            f"***Today***\n"
            f"({datetime.datetime.now().strftime('%Y-%m-%d')})\n\n"
            f"**{city}**\n{curTemp}°C  {wd}\n"
            f"Feels like: {feelsTemp}\n\n"
            f"**Min / Max**\n"
            f"\U0001F53B{minTemp} / {maxTemp}\U0001F53A\n\n"
            f"\U0001F4A7 Humidity: {humidity}%\n\U0001F321 Pressure: {pressure} mmHg\n"
            f"\U0001F32C Wind: {windSpeed} m\s\n\U0001F304 Sunrise: {sunriseTime.strftime('%H:%M')}\n"
            f"\U0001F307 Sunset: {sunsetTime.strftime('%H:%M')}\n\U0000231B Daylight hours: {lenthOfTheDay}\n\n"
            f"***Have a nice day!***")

    except:
        return ("\U00002620 Check the name of the city \U00002620 ")


def getTomorrowWeather(city):  # Weather for Tomorrow
        try:
            data = getData(city, False)

            date = datetime.datetime.today() + datetime.timedelta(days=1)
            curTemp = '{0:+3.0f}'.format(data["list"][1]["main"]["temp"])
            feelsTemp = '{0:+3.0f}'.format(data["list"][1]["main"]["feels_like"])
            maxTemp = '{0:+3.0f}'.format(data["list"][1]["main"]["temp_max"])
            minTemp = '{0:+3.0f}'.format(data["list"][1]["main"]["temp_min"])
            windSpeed = data["list"][1]["wind"]["speed"]

            weatherDisc = data["list"][1]["weather"][0]["main"]
            if weatherDisc in code_to_smile:
                wd = (code_to_smile[weatherDisc])

            return (
                f"***Tomorrow***\n"
                f"({date.strftime('%Y-%m-%d')})\n\n"
                f"**{city}**\n{curTemp}°C  {wd}\n"
                f"Feels like: {feelsTemp}\n"
                f"**Min / Max**\n"
                f"\U0001F53B{minTemp} / {maxTemp}\U0001F53A\n\n"
                f"\U0001F32C Wind: {windSpeed} m\s\n\n"
                f"***Have a nice day!***")

        except:
            return ("\U00002620 Check the name of the city \U00002620 ")


def getFiveDayWeather(city):  # Weather for 5 days
    try:
        data = getData(city, False)

        date = [datetime.datetime.today() +datetime.timedelta(days=2),
                datetime.datetime.today() +datetime.timedelta(days=3),
                datetime.datetime.today() +datetime.timedelta(days=4)]
        maxTemp = []
        minTemp = []
        weatherDisc = []
        wd = []


        for i in data['list']:
            maxTemp.append('{0:+3.0f}'.format(i['main']['temp_max']))
            minTemp.append('{0:+3.0f}'.format(i['main']['temp_min']))
            weatherDisc.append(i['weather'][0]['main'])

        for el in weatherDisc:
            if el in code_to_smile:
                wd.append(code_to_smile[el])


        return (
            f"**{city}**\n\n"
            f"Today {wd[0]}\n"
            f"{minTemp[0]}°C / {maxTemp[0]}°C\n\n"
            f"Tomorrow {wd[1]}\n"
            f"{minTemp[1]}°C / {maxTemp[1]}°C\n\n"
            f"{date[0].strftime('%Y-%m-%d')} {wd[2]}\n"
            f"{minTemp[2]}°C\n\n" # / {maxTemp[2]}°C\n\n"
            f"{date[1].strftime('%Y-%m-%d')} {wd[3]}\n"
            f"{minTemp[3]}°C\n\n"  # / {maxTemp[3]}°C\n\n"
            f"{date[2].strftime('%Y-%m-%d')} {wd[4]}\n"
            f"{minTemp[4]}°C\n\n"  # / {maxTemp[4]}°C\n\n"
            f"***Have a nice day!***")

    except:
        return ("\U00002620 Check the name of the city \U00002620 ")
