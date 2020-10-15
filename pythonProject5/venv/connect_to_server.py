import requests

#This URL will be the URL that your login form points to with the "action" tag.
POST_LOGIN_URL = 'https://my.freecycle.org/login'

#This URL is the page you actually want to pull down with requests.
REQUEST_URL = 'https://my.freecycle.org/home/posts'

payload = {    'username': 'your_username',
    'pass': 'your_password'
}
with requests.Session() as session:
    post = session.post(POST_LOGIN_URL, data=payload)
    r = session.get(REQUEST_URL)
    print(r.text)
    print('Status: ', r.status_code)
    f = open('myfile.html','w+')
    f.write(r.text)
    #or whatever else you want to do with the request data!