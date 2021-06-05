#Dadas duas lista a e b, com n e m elementos respectivamente, mostrar a 
# quantidade de elementos de b que estão também em a.
# ENTRADA (na ordem abaixo)
# - Quantidade de elementos de a
# - Quantidade de elementos de b
# - Elementos de a (um de cada vez)
# - Elementos de b (um de cada vez)
# SAÍDA
# Um inteiro que representa a quantidade de elementos de a que estão em b.
# EXEMPLOS
# Para a entrada n=10, m=4, e as listas a=[1,2,3,4,5,6,7,8,9,10] e b=[5,9,18,20], da seguinte forma:
# 10
# 4
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 5
# 9
# 18
# 20
# A saída deve ser:
# 2
# Para a entrada n=7, m=5, e as listas a=[22,11,10,8,12,76,50] e 
# b=[5,9,76,20,21], lidos de forma semelhante ao exemplo anterior.
# A saída deve ser:
# 1

# -*- coding: utf-8 -*-
n = int(input())
m = int(input())

a = []
b = []
listacontador = []

for i in range(n):
    a.append(int(input()))
for j in range(m):
    b.append(int(input()))

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            listacontador.append(a[i])
print(len(listacontador))