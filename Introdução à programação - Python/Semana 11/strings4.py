'''Qualquer número natural de quatro algarismos pode ser dividido em duas dezenas formadas pelos seus dois primeiros e dois últimos dígitos. Exemplos: 1297: 12 e 97. 5314: 53 e 14. Escreva um programa que imprime todos os milhares (4 algarismos) cuja raiz quadrada seja a soma das dezenas formadas pela divisão acima. Exemplo: raiz de 9801−−−−√=99=98+01. Portanto 9801 é um dos números a ser impresso.

Dica: use as ferramentas de tratamento de strings para facilmente resolver este problema.

 

ENTRADA

- Não possui

SAÍDA

Todos os números que atendem a condição descrita no enunciado (um em cada linha).'''

# -*- coding: utf-8 -*-

for i in range(1000, 10000, 1):

  raiz = float(i) ** 0.5

  i = str(i)
  primeiroPar = i[0]+i[1]
  segundoPar = i[2]+i[3]

  soma = (int(primeiroPar) + int(segundoPar))
  
  if raiz == soma:
    print(i)