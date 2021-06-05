# Dado um polígono convexo de n lados, podemos calcular
# o número de diagonais diferentes nd desse polígono, 
# pela fórmula:

# nd=n(n−3)/2

# Escreva um programa que leia quantos lados tem o polígono e, 
# posteriormente, calcule e mostre a 
# quantidade de diagonais diferentes que o polígono possui.

# Entradas:
# A quantidade n de lados do polígono.

# Saídas:
# A quantidade de diagonais diferentes que o polígono possui, 
# com uma única casa decimal.

# Ex.:
# Entrada	        Saída
# 5               5.0
# 20              170.0

# -*- coding: utf-8 -*- 
n = float(input())
nd = (n*(n-3))/2
print("%.1f" % nd)