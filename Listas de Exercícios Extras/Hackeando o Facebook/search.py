import urllib.request
import json
import os


def search(texto):
    url = 'https://graph.facebook.com/search?q='
    token = os.environ.get('FBTOKEN')
    tail = '&type=post&access_token=' + token
    resp = urllib.request.urlopen(url + texto + tail).read()
    data = json.loads(resp.decode('utf-8'))
    return data['data']

for resp in search('roncaronca'):
    if 'message' in resp:
        print(resp['from']['name'] + ": " + resp['message'] + "\n")
