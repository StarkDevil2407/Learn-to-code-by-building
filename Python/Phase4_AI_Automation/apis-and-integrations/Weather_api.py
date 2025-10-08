import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        print("❌ City not found or API error")
        return

    weather = response["weather"][0]["description"]
    temp = response["main"]["temp"]
    humidity = response["main"]["humidity"]

    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = input("Enter OpenWeatherMap API key: ")
    get_weather(city, api_key)
