1.##Task: JSON Parsing
##write a Python script that reads the students.jon JSON file and prints details of each student.
import json

with open('students.json') as f:
    students = json.load(f)

for s in students:
    print(s)

import requests


API_KEY = 'your_api_key_here'
city = 'Tashkent'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'


response = requests.get(url)
data = response.json()


if response.status_code == 200:
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description.capitalize()}")
else:
    print("Failed to retrieve data:", data.get("message", "Unknown error"))


