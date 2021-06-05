'''Escreva um programa em Python que dados 3 números
quaisquer, mostra esses números em ordem crescente.
Considere que os 3 números são diferentes.

ENTRADA:
3 números

SAÍDA:
Os 3 números em ordem crescente, 1 por linha

Ex.:
Para a entrada:
10
45
2

A saída deve ser:
2
10
45'''

# -*- coding: utf-8 -*-
num1 = float(input())
num2 = float(input())
num3 = float(input())

if num1 > num2 and num2 > num3:
	print('%.0f\n%.0f\n%.0f' % (num3,num2,num1))
if num1 > num3 and num3 > num2:
	print('%.0f\n%.0f\n%.0f' % (num2,num3,num1))
if num2 > num1 and num1 > num3:
	print('%.0f\n%.0f\n%.0f' % (num3,num1,num2))
if num2 > num3 and num3 > num1:
	print('%.0f\n%.0f\n%.0f' % (num1,num3,num2))
if num3 > num1 and num1 > num2:
	print('%.0f\n%.0f\n%.0f' % (num2,num1,num3))
if num3 > num2 and num2 > num1:
    print('%.0f\n%.0f\n%.0f' %(num1,num2,num3))