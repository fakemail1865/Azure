import requests

url = 'https://raw.githubusercontent.com/fakemail1865/Azure/main/testnew%20%5B0.0%5D.xml'

with requests.get(url) as rq:
    payload = rq.content

print(payload)