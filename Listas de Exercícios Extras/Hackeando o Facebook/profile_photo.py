import urllib.request


user = 'calazans10'
url = 'http://graph.facebook.com/' + user + '/picture?type=large'
figure = urllib.request.urlopen(url).read()

arquivo = user + '.jpg'
f = open(arquivo, 'wb')
f.write(figure)
f.close()

print(arquivo, ' gravado no seu diretório')
