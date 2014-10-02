# -*- coding: utf-8 -*-

salario = float(raw_input('Digite o valor do salário: '))
porcentagem = float(raw_input('Digite a porcentagem do aumento: '))

aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento

print "O valor do aumento: R$ %.2f" % aumento
print "O valor do novo salário: R$ %.2f" % novo_salario
