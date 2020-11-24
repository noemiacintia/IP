'''Faça um programa que leia uma String qualquer e retorne as letras da String
(vogais e/ou consoantes) juntamente com a respectiva quantidade de ocorrências de
cada letra. Seu programa deve listar apenas as letras que aparecem pelo menos uma
vez na String de entrada. As letras devem ser listadas sempre em maiúsculas e por
ordem alfabética. Você deve considerar letra minúscula e maiúscula como sendo a mesma
letra maiúscula. Não é necessário tratar letras acentuadas.

ENTRADA
- String de entrada

SAÍDA
- 1ª Letra (maiúscula)
- Quantidade de ocorrências da primeira letra
- 2ª Letra (maiúscula)
- Quantidade de ocorrências da segunda letra
- nª Letra (maiúscula)
- Quantidade de ocorrências da n-ésima letra

EXEMPLOS
Para a entrada:
Casa
A saída deve ser:

A

2

C

1

S

1

 

Para a entrada:

Programacao

 

A saída deve ser:

A

3

C

1

G

1

M

1

O

2

P

1

R

2'''

# -*- coding: utf-8 -*-

string = str(input())
string = string.upper()
string_copia = []
repetidas = []

for i in range(0, len(string), 1):
  if string[i] not in string_copia:
    string_copia.append(string[i])

string_copia.sort()

for pos in range(0, len(string_copia), 1):
  repetidas.append(string.count(string_copia[pos]))

for i in range(0, len(string_copia), 1):
  print(string_copia[i])
  print(repetidas[i])
