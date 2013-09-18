with open('numeros.txt', 'w') as f:
    for linha in range(1, 101):
        f.write("%d\n" % linha)

with open('numeros.txt') as f:
    print (f.read())
