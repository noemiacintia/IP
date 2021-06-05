'''A sequência de Fibonacci é uma das sequências de números bastante famosas. Ela inicia da seguinte forma: 

1,1,2,3,5,8,13,21,...

Sendo que: 

2 é a soma (1+1) 
3 é a soma (1+2) 
5 é a soma (2+3) 
8 é a soma (3+5)
e assim por diante...
Construa um programa que gere uma sequência de Fibonacci de uma quantidade N de elementos. 

 

Entrada 
A entrada consiste em um número inteiro N que indica quantidade de elementos da sequência.

Saída
Seu programa deve imprimir os N primeiros elementos da sequência, um em cada linha.

Entrada	        Saída
1	              1

2                 1
                  1

3                 1
                  1
                  2

6                 1
                  1
                  2
                  3
                  5
                  8

9                 1
                  1
                  2
                  3
                  5
                  8
                  13
                  21
                  34 '''

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Lembre-se de que a correção será automatizada. Logo, é recomendado que, na 
# versão final do seu código (aquela que você deixará como resposta para 
# correção) você use inputs vazios, sem strings [ex: input()] e que os prints 
# na tela não façam nada mais do que o que o enunciado pede. Esteja atento para 
# não inserir pulos de linha adicionais, espaços em branco, ou qualquer outro 
# caractere não esperado. Também esteja atento com a ordem e formatos pedidos 
# nos enunciados para as entradas e saídas. Os enunciados são completos o 
# suficiente para que não fique nenhuma dúvida quanto às entradas e saídas. Os
# exemplos também são mostrados para que você perceba como seu programa deve se
# comportar como um todo (entradas,saídas e processamento). Desde a semana 4, 
# estamos alertando em vários meios (avisos, fóruns, aulas) que a falta de 
# atenção nesses aspectos pode resultar em nota zero ou notas muito baixas, 
# independente da lógica do algoritmo estar correta ou não. Não haverá revisão
# de nota para problemas causados por sua falta de atenção.
# -----------------------------------------------------------------------------

n = int(input())

a = b = 1
f = 0

for i in range(1, n+1, 1):
    if i == 1: 
        print(a)
    elif i == 2:
        print(b)
    else: 
        f = a+b
        a = b
        b = f
        print(f)