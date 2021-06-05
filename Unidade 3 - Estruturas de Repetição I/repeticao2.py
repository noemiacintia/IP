'''Escreva um programa em que dado um inteiro positivo n,
mostre na tela o valor de seu fatorial n!.

ENTRADA:
Um inteiro n.

SAÍDA:
O fatorial de $n$.

EXEMPLO:
Para a entrada 4, a saída deve ser 24.
Para a entrada 5, a saída deve ser 120.
* A saída deve ser apenas o número resultante.'''

# -*- coding: utf-8 -*-
numero = int(input())
fatorial = 1
fator = 1
while fator <= numero:
    fatorial = fatorial * fator
    fator+=1
print(fatorial)