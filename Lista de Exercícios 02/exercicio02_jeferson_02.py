# -*- coding: utf-8 -*-

ano = int(raw_input('Informe o ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    mensagem = 'Ano bissexto com 366'
else:
    mensagem = 'Ano normal com 365'

print mensagem
