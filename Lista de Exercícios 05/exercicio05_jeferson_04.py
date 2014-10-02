# -*- coding: utf-8 -*-


def is_lucky_number(number):
    str_number = str(number)

    if str_number.find("2") != -1 and str_number.find("7") == -1:
        return True
    return False


contador = 0

for i in range(18644, 33088):
    if is_lucky_number(i):
        contador += 1

print contador
