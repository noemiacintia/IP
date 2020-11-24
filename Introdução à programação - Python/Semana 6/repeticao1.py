'''Escreva um programa em Python que receba um inteiro n,
e posteriormente mostre a quantidade de dígitos de n.
Por exemplo: Seja n=123458, a saída deve ser 6.

ENTRADA:
Um inteiro n. (n deve obrigatoriamente ser inteiro).

SAÍDA:
Quantidade de dígitos de n.

Exemplos:
Para n = 20
Saída: 2

Para n = 10234
Saída: 5

Para n = 503
Saída: 3

A saída deve mostrar apenas a quantidade de dígitos de n,
sem qualquer outra mensagem.'''

# -*- coding: utf-8 -*-
valor = int(input())
contaDigitos = 0
if valor == 0:
    contaDigitos = 1
else:
    while valor != 0:
        contaDigitos = contaDigitos + 1
        valor = valor // 10
print(contaDigitos)