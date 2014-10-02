# -*- coding: utf-8 -*-


def inverte(numero):
    inverte = str(numero)[::-1]
    return inverte


numero = int(raw_input('Digite um número inteiro: '))
print 'O número invertido é:', inverte(numero)
