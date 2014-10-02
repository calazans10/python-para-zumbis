import urllib.request
import json
import os

token = os.environ.get('FBTOKEN')
url = 'https://graph.facebook.com/me/friends?access_token=' + token
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))

for amigo in data['data']:
    print(amigo['name'])
