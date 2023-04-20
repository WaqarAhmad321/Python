import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://www.google.com")
print(response.text)
