arquivo = open('numeros.txt', 'w')
for linha in range(1, 101):
    arquivo.write('%d\n' % linha)
arquivo.close()

arquivo = open('numeros.txt', 'r')
for linha in arquivo.readlines():
    print (linha.rstrip())
arquivo.close()
