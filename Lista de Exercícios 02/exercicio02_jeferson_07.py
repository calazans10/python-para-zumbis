# -*- coding: utf-8 -*-

metros = int(raw_input('Informe o tamanho em m² da área a ser pintada: '))

latas = metros / 54

if metros % 54 != 0:
    latas += 1

preco = latas * 80

print 'Quantidade de latas de tinta a serem compradas:', latas
print 'Preço total: R$ %.2f' % preco
