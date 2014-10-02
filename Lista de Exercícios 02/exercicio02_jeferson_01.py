# -*- coding: utf-8 -*-

a = float(raw_input('Informe o valor primeiro lado: '))
b = float(raw_input('Informe o valor segundo lado: '))
c = float(raw_input('Informe o valor terceiro lado: '))

if (a < b + c) and (b < c + a) and (c < b + a):
    print 'É triângulo'

    if a == b and b == c and a == c:
        tipo = 'Triângulo eqüilátero'
    elif (a == b and b != c) or (b == c and c != a) or (a == c and c != b):
        tipo = 'Triângulo isósceles'
    else:
        tipo = 'Triângulo escaleno'

    print tipo
else:
    print 'Não é triângulo'
