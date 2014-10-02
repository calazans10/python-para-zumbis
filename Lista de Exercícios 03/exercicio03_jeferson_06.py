palavra = 'baleia'
troca = ''

for index, item in enumerate(palavra):
    if item in 'aeiou':
        troca += '*'
    else:
        troca += palavra[index]

print (troca)
