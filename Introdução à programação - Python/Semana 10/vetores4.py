'''Dada uma sequência de números inteiros, o valor absoluto (módulo) da diferença entre dois números consecutivos da sequência corresponde à altura do ``degrau'' entre eles. Por exemplo, na seguinte sequência com 7 números [4,0,−1,2,2,3,8]
        
- o degrau do par 4 e 0 tem altura 4;
- o degrau do par 0 e -1 tem altura 1;
- o degrau do par -1 e 2 tem altura 3;
- o degrau do par 2 e 2 tem altura zero;
- o degrau do par 2 e 3 tem altura 1;
- o degrau do par 3 e 8 tem altura 5.
       
        Escreva um programa em Python que lê um inteiro n com (n≥2) e uma sequência com n números inteiros, e imprime a maior altura de um degrau que ocorre na sequência. Por exemplo, na sequência acima, a maior altura de um degrau na sequência é 5.

ENTRADA

- Quantidade de termos n;

- Lista com n termos (um de cada vez).

SAÍDA

- Maior degrau da lista'''

# -*- coding: utf-8 -*-
n = int(input())
while not(n>=2):
    n = int(input())

sequencia = []
degraus = []
resultado = 0

for i in range(n):
    sequencia.append(int(input()))

for j in range(len(sequencia)-1):
    resultado = sequencia[j]-sequencia[j+1]
    if resultado<0:
        resultado*=-1
    degraus.append(resultado)
maior = degraus[0]
for k in range(len(degraus)):
    if degraus[k]>maior:
        maior = degraus[k]
print(maior)