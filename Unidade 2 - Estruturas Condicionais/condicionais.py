'''Escreva um programa em Python que dados 4 números,
mostrar o maior e o menor número. (primeiro o maior depois o menor).

ENTRADA:
4 números

SAÍDA:
2 números: Maior e menor.

Ex.:
Dados os números:
20
10
40
100

A saída deve ser:
100
10'''

# -*- coding: utf-8 -*-
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

maior = num1
menor = num1

if num2 > num1:
    maior = num2
elif num3 > num2:
    maior = num3
if num4 > num3:
    maior = num4

if num2 < num1:
    menor = num2
if num3 < num2:
    menor = num3
if num4 < num3:
    menor = num4
print('%.0f\n%.0f' % (maior, menor))
