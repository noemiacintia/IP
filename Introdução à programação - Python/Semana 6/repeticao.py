'''Escreva um programa em Python que calcule o saldo total de
um investimento, que cresce a uma taxa fixa anual. O programa
deve pedir ao usuário dois valores reais:

Entrada:
- O valor do investimento inicial: Ex: 100, 2500.50
- A taxa de crescimento percentual. Ex: 5% deve ser escrito como 0.05.

Saída
O programa deve mostrar 10 valores reais, que correspondem aos
valores atualizados a cada ano, no total de 10 anos.

Exemplo:
Suponha que o usuário entre com um investimento inicial de
1000 reais com taxa de 4.5% ao ano. Os valores ano a ano que
devem ser mostrados são (com duas casas decimais):

1045.00
1092.03
1141.17
1192.52
1246.18
1302.26
1360.86
1422.10
1486.10
1552.97

DICA
O valor a cada ano deve ser atualizado de acordo com a formula:
investimento = investimento + taxa*investimento
Considerando que a taxa é um valor entre 0 e 1.'''

# -*- coding: utf-8 -*-
from __future__ import division

investimento = float(input())
taxa = float(input())

i = 0

while i < 10:
    investimento = investimento + (taxa*investimento)
    i+=1
    print("%.2f" % investimento)