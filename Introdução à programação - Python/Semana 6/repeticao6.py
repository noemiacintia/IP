'''Desenvolva um algoritmo que receba um número natural na base decimal (10),
converta-o para a base binária (2) e então mostre na tela o resultado da
conversão. Exemplo: Dado 18 a saída deverá ser 10010. A conversão decimal-binário
é realizada com o método de divisões sucessivas, como demonstrado a seguir:

18|_2

(0)  9

---------

9|_2

(1) 4

---------

4|_2

(0) 2

---------

2|_2

(0) 1

---------

1|_2

(1) 0

--------

Observe que os restos obtidos formam o número binário
(o último resto é o primeiro dígito do binário, ou seja, junta-se na ordem inversa).

ENTRADA:
Um número do conjunto dos naturais na base decimal.

SAÍDA:
Um número inteiro na base binária (apenas algarismos 0 e 1).

EXEMPLOS:
Para a entrada: 18
A saída é: 10010

Para a entrada: 95
A saída é: 1011111

* Perceba que seu programa deve apenas exibir o binário resultante e nada mais.'''

# -*- coding: utf-8 -*-

decimal = int(input())

resultado = ''
i = 0

if decimal > 0:
    while decimal > 0: 
        i = decimal % 2
        resultado = resultado + str(i)
        decimal = decimal // 2
    print(resultado[::-1])