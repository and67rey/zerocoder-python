import requests
from pprint import pprint

endpoint = "https://images-api.nasa.gov/search"
query_params = {"q": "Saturn"}
response = requests.get(endpoint, params=query_params)
status = response.status_code
print(status)

res_json = response.json()
pprint(res_json)

n = 1
img = image_path = res_json['collection']['items'][n]['links'][0]['href']
response = requests.get(img)
with open("image.jpg", "wb") as file:
    file.write(response.content)