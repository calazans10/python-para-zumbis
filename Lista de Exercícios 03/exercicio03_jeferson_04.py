# -*- coding: utf-8 -*-


def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


for i in range(13):
    print fibonacci(i)
