# -*- coding: utf-8 -*-

peso = float(raw_input('Informe o peso de peixes: '))
peso_estabelecido = 50
excesso = 0
multa = 0

if peso > peso_estabelecido:
    excesso = peso - peso_estabelecido
    multa = 4 * excesso


print 'Excesso:', excesso
print 'Multa de R$ %.2f' % multa
