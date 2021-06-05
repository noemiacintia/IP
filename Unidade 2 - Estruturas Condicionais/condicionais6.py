'''Dois times, Cormengo e Flaminthians,
participam de um campeonato de futebol,
juntamente com outros times. Cada vitória
conta três pontos, cada empate um ponto.
Fica melhor classificado no campeonato
um time que tenha mais pontos. Em caso
de empate no número de pontos, fica
melhor classificado o time que tiver
maior saldo de gols. Se o número de 
pontos e o saldo de gols forem os
mesmos para os dois times então os 
dois times estão empatados no campeonato. 
Dados os números de vitórias, empates, 
e os saldos de gols dos dois times, sua 
tarefa é determinar qual dos dois está melhor 
classificado, ou se eles estão empatados no campeonato.

Desenvolva um programa que resolva este problema.

ENTRADA:
A entrada: Cv,Ce,Cs,Fv,Fe,Fs que são,
respectivamente, o número de vitórias do
Cormengo, o número de empates do Cormengo,
o saldo de gols do Cormengo, o número de
vitórias do Flaminthians, o número de
empates do Flaminthians e o saldo de gols
do Flaminthians. Leia nesta ordem, uma
variável por vez.

SAÍDA:
Seu programa deve imprimir uma única linha. 
Se Cormengo é melhor classificado que
Flaminthians, a linha deve conter apenas a
letra ‘C’ (sem aspas); se Flaminthians é
melhor classificado que Cormengo, a linha
deve conter apenas a letra ‘F’ (sem aspas);
e se os dois times estão empatados, a linha
deve conter apenas o caractere ‘=' (sem aspas).

Exemplos:
Para a entrada:
10
5
18
11
1
18

A saída deve ser:
C

Para a entrada:
10
5
18
11
2
18

A saída deve ser: 
= '''

# -*- coding: utf-8 -*-
import math
Cvitorias = int(input())
Cempates = int(input())
Csaldo = int(input())
Fvitorias = int(input())
Fempates = int(input())
Fsaldo = int(input())

Cvitorias*=3
Fvitorias*=3
if (Cvitorias+Cempates) > (Fvitorias+Fempates):
    print('C')
if(Cvitorias+Cempates) < (Fvitorias+Fempates):
    print('F')
if(Cvitorias+Cempates) == (Fvitorias+Fempates):
    if Csaldo > Fsaldo:
        print('C')
    elif Csaldo < Fsaldo: 
        print('F')
    elif ((Cvitorias+Cempates) == (Fvitorias+Fempates) and Csaldo == Fsaldo):
        print('=')
