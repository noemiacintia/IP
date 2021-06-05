'''Dado um número natural na base binária b, escreva um programa
para transformá-lo para a base decimal d. 

Exemplo: ao digitar 10010 a saída será 18, pois
1×2^4+0×2^3+0×2^2+1×2^1+0×2^0=18.


ENTRADA:
Um número inteiro na base binária (apenas os algarismos zero e um).

SAÍDA:
Um número inteiro na base decimal.

 
EXEMPLOS:
Para a entrada:
10011
A saída é:
19

Para a entrada:
1110110
A saída é:
118'''

# -*- coding: utf-8 -*-
b = int(input())

resto = i = resultado = 0
num = b

while b > 0:
  resto = b%10
  b = int(b/10)
  i+=1
  resultado += resto *(2**i)
print(int (resultado/2))
