import requests
from pprint import pprint

endpoint = 'https://jsonplaceholder.typicode.com/posts'

params = {"userId": '1'}

response = requests.get(endpoint, params=params)
status = response.status_code
print(status)

res_json = response.json()
pprint(res_json)



