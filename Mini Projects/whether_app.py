import requests
import win32com.client as wi

speaker = wi.Dispatch("SAPI.SpVoice")

api_key = "cf2025979aa8458ab7e130622232903"
query = input("Enter the name of your city: ")
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={query}"
response = requests.get(url)
data = response.json()
temperature = data['current']['temp_c']

speaker.Speak(
    f"The temperature in {query} is {temperature} degree Celsius.")
