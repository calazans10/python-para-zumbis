# -*- coding: utf-8 -*-

metros = int(raw_input('Informe o tamanho em m² da área a ser pintada: '))

litros = metros / 3
latas = litros / 18
preco = latas * 80.00

print 'Quantidade de latas de tinta a serem compradas:', latas
print 'Preço total: R$ %.2f' % preco
