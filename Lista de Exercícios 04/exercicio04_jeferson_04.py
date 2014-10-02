import string


def normalize(text):
    for c in string.punctuation:
        text = text.replace(c, '')
    return text


def has_python(word):
    lista = tuple('python')
    word = word.lower()

    if word.startswith(lista) or word.endswith(lista):
        return True
    return False


texto = "The Python Software Foundation and the global Python community \
welcome and encourage participation by everyone. Our community is based on \
mutual respect, tolerance, and encouragement, and we are working to help each \
other live up to these principles. We want our community to be more diverse: \
whoever you are, and whatever your background, we welcome you."
texto = normalize(texto)
lista = texto.split()

lista_python = []

for palavra in lista:
    if has_python(palavra):
        lista_python.append(palavra)

print (lista_python)
