import random


def embaralha(palavra):
    lista = list(palavra)
    random.shuffle(lista)
    palavra = ''.join(lista)
    return palavra

print (embaralha('abacate'))
print (embaralha('computação'))
