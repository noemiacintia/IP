'''Escreva um programa em Python que encontre 
e mostre as raízes reais de uma equação do 2º
grau da forma ax2+bx+c.

Entrada:
Os coeficientes da equação: a,b,c (nesta ordem)

Saída:
Se Delta>=0, mostrar os valores de x1 e x2 (nesta ordem, um abaixo do outro)

Caso contrário, mostrar a mensagem: "SRR" (sem raízes reais) (mostrar sem as aspas)

Exemplo 1:
Entrada:
1
0
-4

A saída deve ser:
2.00
-2.00

Exemplo 2:
Entrada:
1
1
1

Saída:
SRR'''

# -*- coding: utf-8 -*-
a = float(input())
b = float(input())
c = float(input())

delta = (b**2) - (4*(a)*(c))

if delta >= 0:
    x1 = (-b + (delta**(1/2))) / (2*a)
    x2 = (-b - (delta**(1/2))) / (2*a)
    print('%.2f\n%.2f' % (x1, x2))
else: 
    print('SRR')