# -*- coding: utf-8 -*-

ganha_por_hora = float(raw_input('Quanto ganha por hora: '))
numero_horas = int(raw_input('Número de horas trabalhadas em um mês: '))

salario_bruto = ganha_por_hora * numero_horas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print 'a. + Salário Bruto:   R$ %.2f' % salario_bruto
print 'b. - IR (11%%):        R$ %.2f' % ir
print 'c. - INSS (8%%):       R$ %.2f' % inss
print 'd. - Sindicato (5%%):  R$ %.2f' % sindicato
print 'e. = Salário Líquido: R$ %.2f' % salario_liquido
