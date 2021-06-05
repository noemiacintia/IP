'''Escreva um programa que leia primeiramente um número inteiro n,
e então uma sequência de n números inteiros, um de cada vez.
Seu programa deve calcular o menor e o maior elemento dessa sequência
de n inteiros, exibindo-os na tela, respectivamente e nesta ordem.

Exemplo:

Sejam as entradas:
5
3
4
2
1
-6

A saída correta seria:
-6
4'''

# -*- coding: utf-8 -*-
n = int(input())

num = 0
for i in range(0, n, 1):
  num = int(input())
  if i == 0:
   maior = menor = num
  else:
    if num > maior:
      maior = num
    if num < menor:
      menor = num
print(menor)
print(maior)