# -*- coding: utf-8 -*-

num1 = int(raw_input('Digite o primeiro número: '))
num2 = int(raw_input('Digite o segundo número: '))
num3 = int(raw_input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
elif num3 > num2 and num3 > num1:
    maior = num3
elif num3 == num1 and num2 == num1 and num3 == num2:
    maior = num1
elif num1 == num3 and num3 > num2 and num1 > num2:
    maior = num1
elif num1 == num2 and num1 > num3 and num2 > num3:
    maior = num1

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
elif num3 < num2 and num3 < num1:
    menor = num3
elif num3 == num1 and num2 == num1 and num3 == num2:
    menor = num1
elif num1 == num3 and num3 < num2 and num1 < num2:
    menor = num1
elif num1 == num2 and num1 < num3 and num2 < num3:
    menor = num1

print 'O maior número é:', maior
print 'O menor número é:', menor
