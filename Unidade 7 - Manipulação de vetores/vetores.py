# Escreva um programa em Python, que dadas as idades de n pessoas,
# calcular a média aritmética destas n pessoas.

# ENTRADA
# - A quantidade de pessoas
# - A idade de cada pessoa

# SAÍDA
# - Média aritmética das idades com 2 casas decimais.

# EXEMPLO
# Suponha 4 pessoas, e as idades a seguir:
# 20
# 31
# 18
# 23

# A saída deve ser:
# 23.00

# -*- coding: utf-8 -*-
n = int(input())
mediaAritmetica = []
saida=0

for lista in range(n):
    mediaAritmetica.append(float(input()))

for i in range(len(mediaAritmetica)):
    saida+=mediaAritmetica[i]

saida/=len(mediaAritmetica)

print('%.2f' % saida)