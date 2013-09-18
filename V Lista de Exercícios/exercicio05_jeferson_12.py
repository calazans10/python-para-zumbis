# -*- coding: utf-8 -*-
import string


def normalize(linha):
    linha = linha.lower()
    for c in string.punctuation:
        linha = linha.replace(c, '')
    return linha


dicionario = {}

with open('alice.txt') as f:
    linha = normalize(f.read())
    lista = linha.split()

for word in lista:
    if not word in dicionario:
        dicionario[word] = 1
    else:
        dicionario[word] += 1


print 'Alice aparece %d vezes' % dicionario['alice']
