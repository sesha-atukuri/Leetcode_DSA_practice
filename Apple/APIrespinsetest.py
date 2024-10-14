import requests
import json

response = requests.get("APIurl")
res = json.load(response)
