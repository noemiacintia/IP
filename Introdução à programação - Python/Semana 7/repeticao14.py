'''Escreva um programa que calcule o valor da série abaixo para os n primeiros termos:

S=1/1−2/4+3/9−4/16+5/25−...

 

ENTRADA:
n: Quantidade de termos
Atenção: valide sua entrada para não permitir n negativo.
Enquanto o usuário digitar um valor negativo, seu programa
deve pedir para ele digitar novamente.


SAÍDA:
Valor de S com exatamente 5 casas decimais.


Exemplos:
Para n =10,
0.64563

Para n = 40,
0.68080

Para n=5,
0.78333'''

# -*- coding: utf-8 -*-
n = int(input())
while n < 0: 
  n = int(input())
S = 0 
for i in range(1, n+1, 1):
  if i%2 != 0:
    S += (i / (i * i)) 
  else: 
    S -= (i / (i * i))
print('%.5f' % S)