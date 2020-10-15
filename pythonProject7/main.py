from bs4 import BeautifulSoup
import requests

search = input('Search for: ')
params = {'q': search}
r = requests.get('https://www.worldbank.org/en/search', params=params)
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find("div", {"class": "tab-content"})
links = results.findAll('p', {'class': 'list-group-item-text result-link'})


for item in links:
    item_text = item.find('a').text
    item_herf = item.find('a').attrs['href']
    if item_text and item_herf:
        print(item_text)
        print(item_herf)
        print('Parent: ', item.find('a').parent)

        children = item.children
        for child in children:
            print('Child :',child)