import random


lista = []
lista_par = []
lista_impar = []

for i in range(20):
    num = random.randint(1, 100)
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print ('Números: %s' % str(lista)[1:-1])
print ('Números pares: %s' % str(lista_par)[1:-1])
print ('Números ímpares: %s' % str(lista_impar)[1:-1])
