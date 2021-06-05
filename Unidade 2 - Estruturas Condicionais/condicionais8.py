''' Joãozinho acaba de mudar de escola e a primeira coisa que percebeu na
nova escola é que a gangorra do parquinho não é simétrica, pois uma das
extremidades é mais longa que a outra. Após brincar algumas vezes com um
amigo de mesmo peso, ele percebeu que quando está em uma extremidade, a
gangorra se desequilibra para o lado dele (ou seja, ele fica na parte de
baixo, e o amigo na parte de cima). Porém, quando eles trocam de lado, a
gangorra se desequilibra para o lado do amigo. 

Sem entender a situação, Joãozinho pediu ajuda a outro amigo de outra série,
que explicou que o comprimento do lado interfere no equilíbrio da gangorra,
pois a gangorra estará equilibrada quando:

P1∗C1=P2∗C2 onde P1 e P2 são os pesos da criança do lado esquerdo e direito,
respectivamente, e C1 e C2 são os comprimentos da gangorra do lado esquerdo e
direito, respectivamente. Com a equação, Joãozinho consegue dizer se a gangorra
está equilibrada ou não. No entanto, além disso, ele quer saber para qual lado a
gangorra descerá caso esteja desequilibrada.

Sua missão é desenvolver um algoritmo computacional para resolver esse problema de
Joãozinho, conforme as entradas e saídas especificadas a seguir.

Entradas:
Os valores de P1,C1,P2,C2 (nesta ordem, um por vez).

Saídas:
Caso a gangorra esteja equilibrada, mostre na tela '0' (sem aspas). 
Caso a criança esquerda esteja na parte de baixo, mostre na tela '-1' (sem aspas). 
Caso a criança direita esteja na parte de baixo, mostre na tela '1' (sem aspas). 

Cuidado: a saída do seu programa deve ser mostrada como um texto ('0' e não 0, por exemplo)
e não como um número. Perceba que isso não implica em exibir aspas na saída.

Ex.:
Entrada	       Saída
40
40
38
60              1

50
30
60
25              0 '''

# -*- coding: utf-8 -*-
p1 = float(input())
c1 = float(input())
p2 = float(input())
c2 = float(input())

if (p1*c1) == (p2*c2):
    print('0')
elif (p1*c1) > (p2*c2):
    print('-1')
elif (p1*c1) < (p2*c2):
    print('1')