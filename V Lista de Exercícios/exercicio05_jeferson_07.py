def esconde(mensagem):
    string = ''
    for c in mensagem:
        string += chr(ord(c) + 30000)
    return string


def mostra(mensagem):
    string = ''
    for c in mensagem:
        string += chr(ord(c) - 30000)
    return string

print (esconde('Eu te amo'))
print (mostra('畵疥畐疤疕畐疑疝疟'))
