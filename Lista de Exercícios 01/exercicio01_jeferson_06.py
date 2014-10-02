# -*- coding: utf-8 -*-

distancia = float(raw_input('Digite o valor da distância em m: '))
velocidade = float(raw_input('Digite a velocidade média esperada em km/h: '))

velocidade /= 3.6
tempo = distancia / velocidade

print 'Tempo total da viagem: %.1f' % tempo
