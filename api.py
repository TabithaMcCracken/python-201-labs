import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.delete(base_url + "/588")

print(f"Response Code: {response.status_code}")

response = requests.get(base_url)
pprint(f"Response Content: {response.content}")


