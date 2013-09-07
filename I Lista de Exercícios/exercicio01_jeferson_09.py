# -*- coding: utf-8 -*-

qtd_quilometros = int(raw_input('Quantidade de quilômetros percorrido: '))
qtd_dias = float(raw_input('Quantidade de dias do carro alugado: '))

preco_dias = 60 * qtd_dias
preco_quilometros = 0.15 * qtd_quilometros

total = preco_dias + preco_quilometros

print 'Total a pagar: R$ %.2f' % total
