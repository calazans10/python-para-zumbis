# -*- coding: utf-8 -*-

dias = int(raw_input('Digite o valor em dias: '))
horas = int(raw_input('Digite o valor em horas: '))
minutos = int(raw_input('Digite o valor em minutos: '))
segundos = int(raw_input('Digite o valor em segundos: '))

dias *= 24 * 3600
horas *= 3600
minutos *= 60

total = dias + horas + minutos + segundos


print 'Total em segundos:', total
