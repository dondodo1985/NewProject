import requests
from io import BytesIO
from PIL import Image

params = {'q': 'pizza'}
# r = requests.get('https://google.com/' , params=params)
r = requests.get('https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSVrilc-TrL73JABMbpY3OuhK4suatFilqxVA&usqp=CAU')
print('Status: ', r.status_code)
# print(r.url)
# print(r.text)

# f = open('./page.html', 'w+')
# f.write(r.text)
image = Image.open(BytesIO(r.content))

print(image.size,image.format,image.mode)
path = 'C:/Users/Ragive/Pictures/image.'+image.format
try:
    image.save(path, image.format)
except IOError:
    print('Cannot save image')