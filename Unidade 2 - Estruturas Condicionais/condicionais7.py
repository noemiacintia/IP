# Escreva um programa em Python que dados o peso (em kg)
# e a altura (em metros) de um individuo, nesta ordem,
# calcule o IMC e mostre a situação do mesmo de acordo
# com as definições abaixo:

# IMC=pesoaltura2

# IMC<20 -> ABAIXO

# 20<=IMC<=25 -> NORMAL

# 25<IMC<=30 -> SOBREPESO

# 30<IMC<=40 -> OBESIDADE

# IMC>40 -> OBESIDADE GRAVE

# Entradas
# O peso e a altura (nesta ordem, um por vez).

# Saídas
# A situação

# Exemplos
# Entrada	            Saída
# 90
# 1.80               SOBREPESO

# 97.7
# 1.71               OBESIDADE

# -*- coding: utf-8 -*-
peso = float(input())
altura = float(input())

imc = peso/(altura**2)

if imc < 20:
    print('ABAIXO')
elif imc >= 20 and imc <= 25:
    print('NORMAL')
elif imc > 25 and imc <= 30:
    print('SOBREPESO')
elif imc > 30 and imc <= 40:
    print('OBESIDADE')
elif imc > 40:
    print('OBESIDADE GRAVE')
