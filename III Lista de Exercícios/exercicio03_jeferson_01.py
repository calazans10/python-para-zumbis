# -*- coding: utf-8 -*-

parada = True

while parada:
    nota = int(raw_input('Digite a nota (1 a 10): '))

    if not nota in range(1, 11):
        print 'Valor inválido'
    else:
        print 'Valor válido'
        parada = False
