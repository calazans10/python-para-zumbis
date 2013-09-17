# -*- coding: utf-8 -*-

populacao_a = 80000
populacao_b = 200000
anos = 0

while populacao_a < populacao_b:
    anos += 1
    populacao_a = populacao_a + int(populacao_a * 0.03)
    populacao_b = populacao_b + int(populacao_b * 0.015)

print "Lavará %d anos até que a população do país A ultrapasse ou iguale a \
população do país B." % anos
