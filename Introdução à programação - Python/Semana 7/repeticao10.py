'''Escreva um programa que calcule o valor da série S definida abaixo, com base no número de termos n:

S = 

 

ENTRADAS:
O valor de n. Atenção: n deve ser inteiro e maior ou igual a zero.
Caso o usuário digite um valor negativo para n, seu programa
deve multiplicar n por (-1) antes de realizar o cálculo necessário para S.

SAÍDAS:
O valor de S com 5 casas decimais.


EXEMPLOS:
Entrada	        Saída
20	            55.55253
1	            1.00000
2	            2.50000
0	            0.00000
-5	            8.70000'''

# -*- coding: utf-8 -*-

n = int(input())

if n<0:
    n *= -1
s = 0

for i in range(1, n+1, 1):
    s += i/(n - i + 1)
print('%.5f' % s)