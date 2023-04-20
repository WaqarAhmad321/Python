import requests
import json

query = input("Which type of news you want : ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-02-02&sortBy=publishedAt&apiKey=63c10a6cf38549088b86e56063b38a31"
reponse = requests.get(url)

news = reponse.json()
articles = news['articles']

for article in articles:
    print(f"Title : {article['title']}\nSource : {article['author']}\n")
    print(f"News : {article['description']}")
    print("--------------------------------")
