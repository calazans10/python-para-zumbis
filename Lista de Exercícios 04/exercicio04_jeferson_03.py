import random


lista1 = []
lista2 = []
lista3 = []

for i in range(10):
    lista1.append(random.randint(1, 100))

for i in range(10):
    lista2.append(random.randint(1, 100))

for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print ('Lista 1:', lista1)
print ('Lista 2:', lista2)
print ('Lista 3:', lista3)
