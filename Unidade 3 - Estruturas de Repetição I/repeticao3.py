'''A Olimpíada Internacional de Informática (IOI, no original em inglês)
é a mais prestigiada competição de programação para alunos de ensino médio;
seus aproximadamente 300 competidores se reúnem em um país diferente todo
ano para os dois dias de prova da competição. Naturalmente, os competidores
usamos o tempo livre para acessar a Internet, programar e jogar em seus notebooks,
mas eles se depararam com um problema: o saguão do hotel só tem uma tomada.
Felizmente, os quatro competidores da equipe brasileira da IOI trouxeram cada um
uma régua de tomadas, permitindo assim ligar vários notebooks em uma tomada só;
eles também podem ligar uma régua em outra para aumentar ainda mais o número de
tomadas disponíveis.  No entanto, como as réguas têm muitas tomadas, eles pediram
para você escrever um programa que, dado o número de tomadas em cada régua, determina
quantas tomadas podem ser disponibilizadas no saguão do hotel.


Entrada:
A entrada consiste de quatro variáveis correspondendo a quatro inteiros positivos T1,T2,T3,T4, indicando o número de tomadas de cada uma das quatro réguas. Você deve validar a entrada de cada variável para exigir que Tn seja sempre maior que 1.

Saída:
Seu programa deve imprimir uma única linha contendo um único número inteiro, indicando o número máximo de notebooks que podem ser conectados num mesmo instante.

Exemplos:
Para a entrada: 
2
4
3
2 

A saída deve ser:
8

Para a entrada: 
6
6
6
6

A saída deve ser:
21

Para a entrada:
2
2
2
2

A saída deve ser:
5'''

# -*- coding: utf-8 -*-
import math

T1 = int(input())
while T1 < 1: 
    T1 = int(input())
T2 = int(input())
while T2 < 1: 
    T2 = int(input())
T3 = int(input())
while T3 < 1: 
    T3 = int(input())
T4 = int(input())
while T4 < 1: 
    T4 = int(input())

print((T1-1) + (T2-1) + (T3-1) + T4)