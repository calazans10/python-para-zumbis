# -*- coding: utf-8 -*-

cigarros = int(raw_input('Quantidade de cigarros fumados por dia: '))
anos = int(raw_input('Quantos anos já fumou: '))

dias = anos * 365
total_fumados = dias * cigarros

# um dia tem 24 horas
# a cada cigarro fumado - 10minutos de vida
