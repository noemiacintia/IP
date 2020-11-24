'''Crie uma função potencia que receba dois números a e b (base e expoente, respectivamente) e retorne o valor de ab.

A implementação do programa já está disponível para que você possa testar sua função.


Entrada: 
Já implementada.

Saída:
Já implementada.

 
Exemplos

Entrada	        Saída
2
3                 8


3
2                 9


100
1                100


2
10               1024'''


# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# DEFINA SUA FUNÇÃO A SEGUIR
# -----------------------------------------------------------------------------
def potencia (a, b):
    return a**b
# -----------------------------------------------------------------------------
# NÃO MEXER NAS PRÓXIMAS LINHAS. ELAS SERVEM PRA VOCÊ AVALIAR SUA FUNÇÃO
# -----------------------------------------------------------------------------
print(potencia(int(input()),int(input())))