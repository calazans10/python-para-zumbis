def troca(mensagem):
    troca = ''
    for index, item in enumerate(mensagem):
        if item in 'aeiou':
            troca += '*'
        else:
            troca += mensagem[index]
    return troca


texto = open('mensagem.txt')
saida = open('cripto.txt', 'w')

for linha in texto.readlines():
    saida.write(troca(linha))

texto.close()
saida.close()
