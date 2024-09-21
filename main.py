import requests
from send_email import send_email

api_key = "30a6f116b94b4eb9b3497ae31fa99a81"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-08-21&sortBy=publishedAt&apiKey=30a6f116b94b4eb9b3497ae31fa99a81"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)