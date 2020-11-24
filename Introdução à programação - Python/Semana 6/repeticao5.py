'''Escreva um programa em Python que calcule a aproximação do valor de π
através da fórmula abaixo, considerando os n primeiros termos:

π/2=2/1×2/3×4/3×4/5×6/5×6/7×8/7×8/9...

ENTRADA:
O valor de n: quantidade de termos

SAÍDA:
O valor aproximado de π com 5 casas decimais.

EXEMPLOS:
Entrada	        Saída
10	            3.00218
1000	        3.14002'''


# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n = int(input())

numerador = 0 
denominador = 1
resultado = 1

while n > 0:
    n-=2
    numerador+=2
    resultado *= numerador/denominador 
    denominador+=2
    resultado *= numerador/denominador
print('%.5f' % (resultado*2))