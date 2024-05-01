import requests
from send_email import send_email

# Store the API key and URL Link
api_key = "92c33adb87f44865aa0bc5c8772cb6e4"
url = "https://newsapi.org/v2/everything?" \
      "q=tesla&" \
      "sortBy=publishedAt&" \
      "apiKey=92c33adb87f44865aa0bc5c8772cb6e4&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

article_list = []

body = ""
# Access the article titles and descriptions
for article in content["articles"][:20]:
    if article["title"] and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)