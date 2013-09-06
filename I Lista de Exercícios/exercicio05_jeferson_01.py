# -*- coding: utf-8 -*-

preco = float(raw_input('Digite o preço do produto: '))
percentual = float(raw_input('Digite o percentual de desconto: '))

desconto = preco * (percentual / 100)
novo_preco = preco - desconto

print "O valor do desconto: R$ %.2f" % desconto
print "O preço do produto a pagar: R$ %.2f" % novo_preco
