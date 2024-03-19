import requests

url = 'https://the-one-api.dev/v2/'

response = requests.get(url)

data = response.json()

print(data['value'])