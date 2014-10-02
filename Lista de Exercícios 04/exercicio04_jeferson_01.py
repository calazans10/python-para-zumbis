import random


def maior(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior


def menor(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor


array = []

for i in range(10):
    array.append(random.randint(1, 100))

print ('Maior número:', maior(array))
print ('Menor número:', menor(array))
