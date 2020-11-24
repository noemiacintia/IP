'''Fulaninho é um menino que gosta muito de ver televisão.
No entanto ele se depara com um problema muito chato. Sempre
que começa um novo programa no canal preferido dele, acontece
de o volume do som deste programa está diferente do anterior,
às vezes com volume menor, outras vezes com volume maior. 

Quando está com volume menor, ele aumenta o volume pressionando
uma quantidade de vezes seguidas o botão de aumentar para o volume
ficar ideal. A mesma coisa acontece quando está um volume maior, e 
ele diminui o volume pressionando alguma quantidade de vezes seguidas 
o botão de diminuir o volume para ficar com o volume que ele goste no 
momento.

O aparelho de TV de Fulaninho tem umas peculiaridades: ele possui 
volume mínimo, com valor 0 (também chamado de mudo, ou "mute", já que 
a TV dele é importada), e volume máximo, com valor 100. A TV nunca 
ultrapassa os volumes máximo e mínimo. Por exemplo: se o volume já estiver 
no máximo e ele pressionar o botão de aumentar o som, o volume não se altera. 
Da mesma forma, se o volume estiver no valor mínimo e ele pressionar o botão 
de diminuir o som, o volume não se altera.

Fulaninho está precisando da sua ajuda: ele lembra qual era o volume 
inicial da TV, e quantas vezes ele pressionou cada botão. Mas, como 
foram várias mudanças de volume, ele não sabe qual é o volume atual 
da TV. Por isso, pediu que você o ajude a calcular qual é o volume 
atual, dados o volume inicial e a lista de trocas de volume que ele 
realizou. Você, como um programador desenrolado e muito empolgado, 
logo pensou em fazer um pequeno programa que ajude Fulaninho e 
outras pessoas que estejam passando por problema parecido.

 

ENTRADAS
As duas primeiras entradas do seu programa são: V e T 
(nesta ordem, uma de cada vez). V e T são números inteiros 
que indicam, respectivamente, o volume inicial e o número 
de trocas de volume.

Em seguida, seu programa deve pedir outras T entradas, 
uma por vez, de como que cada uma dessas entradas seja 
um número inteiro ti indicando uma modificação de volume 
realizada. Os valores dessas T entradas devem ser lidos na 
ordem em que estas modificações de volume foram feitas pelo 
usuário. O primeiro número indica a primeira modificação 
de volume, o segundo número indica a segunda modificação, 
e assim por diante. Para cada modificação ti, um número 
maior do que zero significa quantas vezes Bruno pressionou 
o botão de aumentar o som da TV; um número menor do que zero 
significa quantas vezes ele pressionou o botão de diminuir 
o som da TV. Ou seja, se o número é igual a 5, significa que 
nessa modificação ele pressionou cinco vezes o botão de aumentar 
o som; se o número é igual a -3, significa que nessa modificação 
ele pressionou o botão de diminuir o som três vezes.

 

SAÍDAS
Seu programa deve imprimir apenas uma linha, contendo apenas um inteiro F,
que indica qual o volume atual da TV após todas as mudanças de volume realizadas
pelo usuário, considerando o volume inicial da TV e todas as trocas a partir de então.

 

EXEMPLOS:
Entrada
50
4
11
20
-15
-13

Saída
53
	
 

Entrada
50 
5
30
30
30
40
-78

Saída
22'''

# -*- coding: utf-8 -*-

V = int(input())
T = int(input())

vf = V

for i in range(0, T, 1):
    T2 = int(input())
    vf += T2
    
    if vf<0:
        vf = 0
    elif vf>100:
        vf = 100
print(vf)
