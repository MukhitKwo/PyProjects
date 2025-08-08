import requests
import json

with open("keys.json", "r") as f:
    keys = json.load(f)

apikey = keys["tomorrow_io"]["api_key"]
location = "aveiro"

url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={apikey}"

headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
}

response = requests.get(url, headers=headers)

data = response.json()

temp = data["data"]["values"]["temperature"]
humidity = data["data"]["values"]["humidity"]
rain_prob = data["data"]["values"]["precipitationProbability"]

print(temp)
print(humidity)
print(rain_prob)


