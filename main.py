import requests


# Store the API key and URL Link
api_key = "92c33adb87f44865aa0bc5c8772cb6e4"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2024-03-27&sortBy=publishedAt&apiKey=92" \
      "c33adb87f44865aa0bc5c8772cb6e4"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
      print(article["title"])
      print(article["description"])