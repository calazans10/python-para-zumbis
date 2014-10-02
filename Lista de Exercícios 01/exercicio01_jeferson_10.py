# -*- coding: utf-8 -*-

cigarros = int(raw_input('Quantidade de cigarros fumados por dia: '))
anos = int(raw_input('Quantos anos já fumou: '))

dias = anos * 365
total_fumados = dias * cigarros
total_dia = 24 * 6

total_dias_perdidos = total_fumados / total_dia

print 'Total de dias perdidos',  total_dias_perdidos
