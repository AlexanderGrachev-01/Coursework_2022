import requests
import datetime
from config import open_weather_token, code_to_smile

def getWeather(city, get_weather_token):
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

def main():
    city = input("Enter the city: ")
    getWeather(city, open_weather_token)


if __name__ == '__main__':
    main()