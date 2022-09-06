import requests 
from bs4 import BeautifulSoup # to read xml file


# Reading the data inside the xml
# file to a variable under the name
# data

url = "https://raw.githubusercontent.com/fakemail1865/new_rep/main/FinalTest%20%5B0.1%5D.xml"

with requests.get(url) as rq:
    payload = rq.content

headers = {
  'Content-Type': 'application/octet-stream',
  'Authorization': 'Basic c2VtYWRtaW46c2VtYWRtaW4=',
  'Cookie': 'XSRF-TOKEN=a3dc895f-3443-4952-8d6e-a492d2218e14'
}

#send post request to semarchy
name = "testnew"  # name of model you want to import
key = 0.0 
url = "http://20.24.242.37/semarchy/api/rest/app-builder/models/{name}/editions/{key}/content".format(name=name,key=key)

response = requests.request("POST", url,  headers=headers, data=payload)

print(response)
