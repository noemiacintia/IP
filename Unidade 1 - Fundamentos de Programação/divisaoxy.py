# Escreva um programa, que dados dois números reais x e y
# (nesta ordem), mostra o resultado da divisão xy com 5
# casas decimais.

# Entradas:
# O programa deve pedir ao usuário dois valores reais: x e y (nesta ordem).

# Saídas:
# O programa deve exibir o resultado da divisão de x por y, com 5 casas decimais.

# Ex.:

# E: 26
# E: 17
# S: 1.52941

# E: 4
# E: 3
# S: 1.33333

# -*- coding: utf-8 -*-
x = float(input("Digite o valor x: "))
y = float(input("Digite o valor y: "))
divisao = x/y
print('%.5f' % divisao)