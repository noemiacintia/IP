'''Um conjunto numérico de valores é dito lecker se um e apenas
um elemento do conjunto é maior que seus vizinhos. 

Escreva um programa que verifique se uma sequencia de
4 números dados é ou não lecker. O programa deve obrigatoriamente
responder 'S' (Sim, é lecker) ou 'N' (não é lecker). 

Dica: Os 4 valores devem ser armazenados em quadro variáveis
distintas e lidos um de cada vez.

Exemplos:
Entrada	            Saída	            Justificativa para a saída gerada
2
5
10
46	                  S                 O resultado é SIM, pois apenas o 46 é maior que seus vizinhos.


16
16
16
16	                  N                 Nenhum elemento é maior que seus vizinhos.


4
7
1
10	                  N                 7 e 10 são maiores que seus respectivos vizinhos.


4
7
5
3	                  S                 Apenas o 7 é maior que seus vizinhos.


1
1
2
1	                  S                 Apenas o 2 é maior do que os vizinhos.'''


# -*- coding: utf-8 -*-
import math

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

i = 0
if (num2 == num1 and num2 == num3) and (num3 == num2 and num3 == num4):
    print('N')
elif (num2 > num1 and num2 < num3) and (num3 > num2 and num3 < num4):
    print('S')
elif (num2 > num1 and num2 > num3) and (num3 < num2 and num3 < num4):
    print('N')
elif (num2 > num1 and num2 > num3) and (num3 < num2 and num3 > num4):
    print('S')
elif (num2 == num1 and num2 < num3) and (num3 > num2 and num3 > num4):
    print('S')
elif (num2 == num1 and num2 == num3) and (num3 == num2 and num3 < num4):
    print('S')
elif (num2 < num1 and num2 < num3) and (num3 > num2 and num3 < num4):
    print('N')
elif (num2 < num1 and num2 < num3) and (num3 > num2 and num3 == num4):
    print('S')
elif (num2 == num1 and num2 == num3) and (num3 == num2 and num3 > num4):
    print('N')