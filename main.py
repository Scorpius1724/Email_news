import requests


api_key = "92c33adb87f44865aa0bc5c8772cb6e4"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2024-03-27&sortBy=publishedAt&apiKey=92" \
      "c33adb87f44865aa0bc5c8772cb6e4"
request = requests.get(url)
content = request.text
print(content)