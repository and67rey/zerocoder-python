import requests
from pprint import pprint

endpoint = 'https://jsonplaceholder.typicode.com/posts'

data = {'title': 'foo', 'body': 'bar', 'userId': 1}

response = requests.post(endpoint, data=data)
status = response.status_code
print(status)

res_json = response.json()
pprint(res_json)