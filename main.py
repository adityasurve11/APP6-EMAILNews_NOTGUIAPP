import requests
from send_email import send_email

api_key = "30a6f116b94b4eb9b3497ae31fa99a81"
url = "https://newsapi.org/v2/top-headlines?" \
      "country=us&" \
      "category=business&" \
      "apiKey=30a6f116b94b4eb9b3497ae31fa99a81"

request = requests.get(url)
content = request.json()

body = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    if (article["description"] is not None) and (article["title"] is not None):
        body = body + article["title"] + "\n"\
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)