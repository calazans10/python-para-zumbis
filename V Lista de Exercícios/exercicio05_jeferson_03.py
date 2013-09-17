# -*- coding: utf-8 -*-

contador = 0

for i in range(1067, 3628):
    if i % 2 == 0 and i % 7 == 0:
        contador += 1

print contador
