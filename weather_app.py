import requests

def get_weather(city):
    API_KEY = "your_api_key_here"  # 🔑 get it free from https://openweathermap.org/api
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"🌤️ Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description'].title()}")
    else:
        print("❌ City not found. Please check the spelling.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
