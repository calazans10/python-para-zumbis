# -*- coding: utf-8 -*-


def algoritmo_de_euclides(num1, num2):
    if num2 == 0:
        return num1
    else:
        return algoritmo_de_euclides(num2, num1 % num2)


print algoritmo_de_euclides(348, 156)
