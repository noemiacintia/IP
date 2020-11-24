'''Dizemos que uma sequência com pelo menos 3 números inteiros e sem elementos consecutivos iguais é um pico, se tem um pedaço inicial crescente (estritamente) depois fica decrescente (estritamente) até o final. Implemente um programa que recebe uma lista de números inteiros e verifica se essa lista forma ou não um pico.

Veja os exemplos:

[1,2,1] é um pico, pois tem o pedaço inicial crescente [1,2] e depois decresce.
[1,5,3] é um pico, pois tem o pedaço inicial crescente [1,5] e depois decresce.
[2, 5, 10, 46, 25, 12, 7] é um pico, pois tem o pedaço inicial crescente [2, 5, 10, 46] e depois só decresce.
[13, 5, 4, 12, 3, 0, -3, -14] não é um pico, pois o seu pedaço inicial [13, 5] é decrescente.
[6, 7, 8, 9, 10] não é um pico, pois tem apenas um pedaço crescente.
[10, 9, 7, 4] não é um pico, pois tem apenas um pedaço decrescente.
[1, 2, 1, 2, 1, 2, 1] não é um pico, pois depois do pedaço inicial crescente [1, 2] não decresce até o final.
Você deve definir e utilizar pelo menos uma função em sua solução. Do contrário, receberá nota zero, mesmo que o programa seja avaliado com alguma nota positiva.

Dica: aproveite a estrutura que já é oferecida no editor de código ao iniciar sua implementação.

  

Entrada 
A quantidade inteira n de elementos da lista, e os n elementos inteiros que foram essa lista, nessa ordem, um de cada vez.

 

Saída
Exibir "S" (sem aspas), se a lista informada é um pico. Exibir "N" (sem aspas), caso contrário.
 
Exemplos

Entrada	            Saída
3
1
5
3                   S


8
13
5
4
12
3
0
-3
-14                  N


4
1
2
1
2                   N '''

# -*- coding: utf-8 -*-
def pico(lista):
    x = maiorIndice = 0
    maior = max(lista)
    
    for i in range(0, n):
        if lista[i] == maior:
            maiorIndice = i
    if n<3 or maior == lista[0] or maior == lista[n-1]:
        return False
    
    for j in range(1, maiorIndice+1):
        if lista[j-1] > lista[j] or lista[j-1] == lista[j]:
            x+=1
    
    for k in range(maiorIndice+1, n):
        if lista[k-1] < lista[k] or lista[k-1] == lista[k]:
            x+=1
    
    if not(x==0):
        return False
    return True

# programa principal daqui pra baixo
n = int(input())
# CONTINUE...
lista = []

for i in range(0, n):
    lista.append(int(input()))

if not(pico(lista)):
    print('N')
else:
    print('S')