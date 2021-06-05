'''Crie uma função c2f, que recebe como parâmetro uma temperatura em graus
Celsius e retorna o valor dessa temperatura convertido em Fahrenheit.

A implementação do programa já está disponível para que você possa testar sua função.

Entrada: 
Já implementada.

Saída:
Já implementada.

 
Exemplos:
Entrada	        Saída
30              86.0

0               32.0

100             212.0'''

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# DEFINA SUA FUNÇÃO A SEGUIR
# -----------------------------------------------------------------------------
def c2f(celsius):
    return (celsius*(9/5))+32
# -----------------------------------------------------------------------------
# NÃO MEXER NAS PRÓXIMAS LINHAS. ELAS SERVEM PRA VOCÊ AVALIAR SUA FUNÇÃO
# -----------------------------------------------------------------------------
print(c2f(float(input())))