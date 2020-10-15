# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
try:
    import simplejson as json
except ImportError:
    import json

import os

# check if file exists and not empty
if os.path.isfile('./ages.json') and os.stat("./ages.json").st_size !=0:
    old_file = open('./ages.json', 'r+')
    data = json.loads(old_file.read())
    print('Current age is ', data['age'], 'adding a year.')
    data['age'] = data['age'] + 1
    print('New age is ', data['age'])

else:
    old_file = open('./ages.json', 'w+')
    data = {'name': 'James', 'age': 35}
    print('No file found, setting default age to:',data['age'] )

old_file.seek(0)
old_file.write(json.dumps(data))

"""newfile = open('newfile.txt', 'w+')

string = 'this is the content that will be written in the text file.'

newfile.write(string)"""