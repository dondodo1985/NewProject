import requests
import simplejson as json

url = "https://en.wikipedia.org/wiki/Jason_Statham"
#payload = {"longurl", "http://example.com"}
#headers = {"Content-Type":"application/json"}
#r = requests.post(url, json=payload, headers=headers)
#print(json.loads(r.text)["error"]["code"])
response = requests.get(url)
html = response.text
print(html)