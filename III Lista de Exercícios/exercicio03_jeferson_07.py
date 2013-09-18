data = input('Data de nascimento: ')
dia, mes, ano = data.split('/')

meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio',
         6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro',
         11: 'Novembro', 12: 'Dezembro'}

print ('Você nasceu em:')
print ('%s de %s de %s' % (dia, meses[int(mes)], ano))
