# Escrever um programa, que dada uma temperatura
# em graus Celsius, calcule e mostre a temperatura
# convertida para graus Fahrenheit.

# Fórmula de conversão: f=(9c+160)/5

# Entradas:
# A temperatura em graus Celsius (use o tipo de dado adequado).

# Saídas:
# A temperatura em graus Fahrenheit, com 2 casas decimais.

# Ex.:
# Entrada	        Saída
# 30                86.00
# 64.4              147.92

# -*- coding: utf-8 -*-
celsius = float(input("Digite a temperatura em °C: "))
fahrenheit = ((9*celsius)+160)/5
print('%.2f' % fahrenheit)