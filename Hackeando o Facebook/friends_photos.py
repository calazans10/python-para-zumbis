from gender import female
import urllib.request
import json
import os


def grava_imagem(amigo):
    size = '/picture?width=200&height=200'
    url = 'http://graph.facebook.com/' + amigo['id'] + size
    figura = urllib.request.urlopen(url).read()
    f = open(amigo['name'] + '.jpg', 'wb')
    f.write(figura)
    f.close()
    print(amigo['name'], '.jpg impresso')

token = os.environ.get('FBTOKEN')
url = 'https://graph.facebook.com/me/friends?access_token=' + token
resp = urllib.request.urlopen(url).read()
dados = json.loads(resp.decode('utf-8'))

for amigo in dados['data']:
    if female(amigo['id']):
        grava_imagem(amigo)
