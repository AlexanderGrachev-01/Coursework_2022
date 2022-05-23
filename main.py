import requests
import datetime
from pprint import pprint
from config import open_weather_token

def getWeather(city, get_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        curWeather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        windSpeed = data["wind"]["speed"]
        sunriseTime = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunsetTime = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenthOfTheDay = sunsetTime - sunriseTime

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H-%M')}***\n"
              f"Weather in: {city}\nTemperature: {curWeather}°C\n"
              f"Humidity: {humidity}%\nPressure: {pressure} mmHg\n"
              f"Wind: {windSpeed} m\s\nSunrise: {sunriseTime}\n"
              f"Sunset: {sunsetTime}\nDaylight hours: {lenthOfTheDay}\n"
              f"Have a nice day!")

    except Exception as ex:
        print(ex)
        print("Check the name of the city")

def main():
    city = input("Enter the city: ")
    getWeather(city, open_weather_token)


if __name__ == '__main__':
    main()