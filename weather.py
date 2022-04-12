import requests
# pip3 install requests >>> in terminal
# API data from Current weather data
API_KEY = "33d4cb81f5a78858df7963c310333999"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
city = input("Enter a city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}" # q stands for query
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather: ", weather)
    print("Temperature: ", temperature, "celsius")
else:
    print("error")

