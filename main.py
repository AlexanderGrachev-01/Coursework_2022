import requests
import datetime
import pprint
from config import open_weather_token, code_to_smile

def getWeather(city):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={open_weather_token}"
        )
        data = r.json()
        print(data)

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

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H-%M')}***\n"
              f"{city} {wd}\nTemperature: {curTemp}°C\n"
              f"Humidity: {humidity}%\nPressure: {pressure} mmHg\n"
              f"Wind: {windSpeed} m\s\nSunrise: {sunriseTime}\n"
              f"Sunset: {sunsetTime}\nDaylight hours: {lenthOfTheDay}\n"
              f"Have a nice day!")

    except Exception as ex:
        print(ex)
        print("Check the name of the city")


def getDayWeather(city):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={open_weather_token}"
        )
        data = r.json()
        print(data)

        city = data["name"]
        curTemp = data["main"]["temp"]
        feelsTemp = data[""]
        maxTemp = data[""]
        minTemp = data[""]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        windSpeed = data["wind"]["speed"]
        sunriseTime = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunsetTime = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenthOfTheDay = sunsetTime - sunriseTime

        weatherDisc = data["weather"][0]["main"]
        if weatherDisc in code_to_smile:
            wd = code_to_smile[weatherDisc]

        print(#f"***{datetime.datetime.now().strftime('%Y-%m-%d %H-%M')}***\n"
              f"{city}\n{curTemp}°C  {wd}\n\n"
              f"Feels like: {feelsTemp}\n"
              f"Max: {maxTemp} / min: {minTemp}\n\n"
              f"\U0001F4A7 Humidity: {humidity}%\n\U0001F321 Pressure: {pressure} mmHg\n"
              f"\U0001F32C Wind: {windSpeed} m\s\n\U0001F304 Sunrise: {sunriseTime.strftime('%H:%M')}\n"
              f"\U0001F307 Sunset: {sunsetTime.strftime('%H:%M')}\n\U0000231B Daylight hours: {lenthOfTheDay}\n\n"
              f"***Have a nice day!***")

    except Exception as ex:
        print(ex)
        print("Check the name of the city")


def getFiveDayWeather(city):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={open_weather_token}"
        )
        data = r.json()
        print(data)

        city = data["name"]
        maxTemp1 = data[""]
        minTemp1 = data[""]
        weatherDisc1 = data["weather"][0]["main"]
        if weatherDisc1 in code_to_smile:
            wd1 = code_to_smile[weatherDisc1]
        maxTemp2 = data[""]
        minTemp2 = data[""]
        weatherDisc2 = data["weather"][0]["main"]
        if weatherDisc2 in code_to_smile:
            wd2 = code_to_smile[weatherDisc2]
        maxTemp3 = data[""]
        minTemp3 = data[""]
        weatherDisc3 = data["weather"][0]["main"]
        if weatherDisc3 in code_to_smile:
            wd3 = code_to_smile[weatherDisc3]
        maxTemp4 = data[""]
        minTemp4 = data[""]
        weatherDisc4 = data["weather"][0]["main"]
        if weatherDisc4 in code_to_smile:
            wd4 = code_to_smile[weatherDisc4]
        maxTemp5 = data[""]
        minTemp5 = data[""]
        weatherDisc5 = data["weather"][0]["main"]
        if weatherDisc5 in code_to_smile:
            wd5 = code_to_smile[weatherDisc5]

        print(f"{city}\n\n"
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

    except Exception as ex:
        print(ex)
        print("Check the name of the city")


def test_weather(city):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        print(data)

        date = []
        maxTemp = []
        minTemp = []
        weatherDisc = []
        wd = []



        for i in data['list']:
            print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])



        for i in data['list']:
            maxTemp.append(i['main']['temp_max'])
            minTemp.append(i['main']['temp_min'])
            weatherDisc.append(i['weather'][0]['main'])

        print(maxTemp[0], maxTemp[1], maxTemp[2], maxTemp[3], maxTemp[4])
        print(minTemp[0], minTemp[1], minTemp[2], minTemp[3], minTemp[4])
        print(weatherDisc[0], weatherDisc[1], weatherDisc[2], weatherDisc[3], weatherDisc[4])

        for el in weatherDisc:
            if el in code_to_smile:
                wd.append(code_to_smile[el])

        for el in wd:
            print(el)

    except:
        print ("\U00002620 Check the name of the city \U00002620 ")

def test_tomorrow(city):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint.pprint(data)

        date = datetime.datetime.today() + datetime.timedelta(days=1)
        curTemp = '{0:+3.0f}'.format(data["list"][1]["main"]["temp"])
        feelsTemp = '{0:+3.0f}'.format(data["list"][1]["main"]["feels_like"])
        maxTemp = '{0:+3.0f}'.format(data["list"][1]["main"]["temp_max"])
        minTemp = '{0:+3.0f}'.format(data["list"][1]["main"]["temp_min"])
        windSpeed = data["list"][1]["wind"]["speed"]

        weatherDisc = data["list"][1]["weather"][0]["main"]
        if weatherDisc in code_to_smile:
            wd = (code_to_smile[weatherDisc])

        print(
            f"*Tomorrow*\n"
            f"({date})\n\n"
            f"{city}\n{curTemp}°C  {wd}\n"
            f"Feels like: {feelsTemp}\n\n"
            f"**Min / Max**\n"
            f"{minTemp} / {maxTemp}\n\n"
            f"\U0001F32C Wind: {windSpeed} m\s\n"
            f"***Have a nice day!***")

    except:
        print ("\U00002620 Check the name of the city \U00002620 ")

def main():
    city = input("Enter the city: ")
    test_tomorrow(city)


if __name__ == '__main__':
    main()