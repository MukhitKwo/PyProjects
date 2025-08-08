import requests
from dotenv import load_dotenv
import os
import json

load_dotenv(dotenv_path="config/.env")

apikey = os.getenv("TOMOROW_IO_API_KEY")
location = "aveiro"

url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={apikey}"

headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
}

response = requests.get(url, headers=headers)

data = response.json()

print(json.dumps(data, indent=4))


temp = data["data"]["values"]["temperature"]
humidity = data["data"]["values"]["humidity"]
rain_prob = data["data"]["values"]["precipitationProbability"]

# print(temp)
# print(humidity)
# print(rain_prob)
