# Escreva um programa em Python que peça ao usuário uma lista com n valores e calcule:
# - O somatório dos números ímpares;
# - O somatório dos números pares;
# - A quantidade de números ímpares;
# - A quantidade de números pares;
# ENTRADA
# - Um valor de n;
# - Uma lista com n valores (um lido por vez);
# SAÍDA
# - O somatório dos números ímpares;
# - O somatório dos números pares;
# - A quantidade de números ímpares;
# - A quantidade de números pares;
# - A lista completa
# EXEMPLO
# Seja n=10 e a lista: 
# 10
# 11
# 20
# 22
# 30
# 33
# 40
# 44
# 50
# 55
# A saída deve ser (na ordem definida acima):
# 99
# 216
# 3
# 7
# [10, 11, 20, 22, 30, 33, 40, 44, 50, 55]

# -*- coding: utf-8 -*-
n = int(input())

lista = []
pares = impares = 0
listapares = []
listaimpares = []

for i in range(n):
    lista.append(int(input()))

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares+=lista[i]
        listapares.append(lista[i])
    else:
        impares+=lista[i]
        listaimpares.append(lista[i])
print(impares)
print(pares)
print(len(listaimpares)) 
print(len(listapares))
print(lista)
