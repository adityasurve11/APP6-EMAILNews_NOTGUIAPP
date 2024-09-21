import requests

api_key = "30a6f116b94b4eb9b3497ae31fa99a81"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-08-21&sortBy=publishedAt&apiKey=30a6f116b94b4eb9b3497ae31fa99a81"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])