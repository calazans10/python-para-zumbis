import urllib.request
import json


def female(id_friend):
    url = 'http://graph.facebook.com/' + id_friend
    resp = urllib.request.urlopen(url).read()
    data = json.loads(resp.decode('utf-8'))

    if 'gender' not in data:
        return False
    return data['gender'] == 'female'
