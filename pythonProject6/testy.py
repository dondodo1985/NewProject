import requests
#import xml.etree.ElementTree as ET
url = 'https://httpbin.org/get'
payload = {'page': 2, 'count': 25}
response = requests.get(url, params=payload,timeout=3)
#country_data = response.text
print(response.headers)
print(response.text)
print(response.status_code)
print(response.url)
params= {'username': 'corey', 'password':'testing'}
r = requests.post('https://httpbin.org/post',data=params)
r_dict = r.json()
print(r_dict['form'])
#countries = ET.fromstring(country_data)
#(countries)