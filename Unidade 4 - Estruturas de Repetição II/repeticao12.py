'''Escreva um programa em Python que dado um inteiro,
mostre todos os seus divisores positivos (exceto 1 e ele mesmo),
e ao final mostrar se o número é ou não primo.

ENTRADA:
Um inteiro n

SAÍDA
Os divisores positivos (um por linha, em ordem crescente)
"PRIMO" (sem aspas), se o n é um número primo. 
"NÃO PRIMO" (sem aspas), caso n não seja um número primo. 



EXEMPLOS:

Para a entrada:
16
A saída deve ser:
2
4
8
NÃO PRIMO

Para a entrada:
17
A saída deve ser:
PRIMO

Para a entrada:
-11
A saída deve ser:
PRIMO'''

# -*- coding: utf-8 -*-

n = int(input())
multiplo = 0

if n < 0:
  n = n * -1
  
for i in range(2, n):
    if n%i == 0:
        print(i)
        multiplo += 1
if multiplo == 0:
    print("PRIMO")
else:
    print("NÃO PRIMO")