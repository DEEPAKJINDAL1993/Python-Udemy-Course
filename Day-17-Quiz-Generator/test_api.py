import requests
import json

url = 'https://opentdb.com/api.php?amount=10&category=22&difficulty=medium&type=boolean'
response = requests.get(url)

print(response.json())