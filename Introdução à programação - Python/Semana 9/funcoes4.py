'''Implemente as seguintes funções conforme estritamente especificado a seguir:

leiaNumero, que recebe como parâmetro uma string a ser usada para pedir um dado ao usuário,
lê um número real digitado pelo usuário e retorna esse valor lido
escreva, que recebe como parâmetro uma variável e se encarrega de exibir seu valor na tela 
media, que recebe quatro números reais a,b,c e d como parâmetros e retorna o valor da média ponderada: (a+3b+2c+d)/7
variacao, que recebe quatro números reais a,b,c e d como parâmetros e retorna a 
maior variação (distância) entre os números, ou seja, a diferença entre o maior e 
o menor dos quatros números informados

A implementação do programa já está disponível para que você possa testar sua função.

  

Entrada 
Já implementada.

Saída
Já implementada.

 
Exemplos
Entrada	            Saída
2
2
2
2                   2.0
                    0.0

1.0
2.0
3.0
4.0                 2.4
                    3.0

10.0
8.0
9.5
8.2                 8.7
                    2.0 '''

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# DEFINA SUA FUNÇÃO A SEGUIR
# -----------------------------------------------------------------------------

def leiaNumero(x):
    x = float(input())
    return x

def escreva(y):
    print('%.1f' % y)
    return

def media(a, b, c, d):
    mediaPonderada = (a+(3*b)+(2*c)+d)/7
    return mediaPonderada

def variacao(a, b, c, d):
    maior = menor = 0.0
    if a>b and a>c and a>d:
        maior=a
    elif b>a and b>c and b>d:
        maior=b
    elif c>a and c>b and c>d:
        maior = c
    elif d>a and d>b and d>c:
        maior = d
    
    if a<b and a<c and a<d:
        menor=a
    elif b<a and b<c and b<d:
        menor=b
    elif c<a and c<b and c<d:
        menor = c
    elif d<a and d<b and d<c:
        menor = d
    return maior-menor

# -----------------------------------------------------------------------------
# NÃO MEXER NAS PRÓXIMAS LINHAS. ELAS SERVEM PRA VOCÊ TESTAR SUA FUNÇÃO E PARA
# O CORRETOR AUTOMATIZADO AVALIAR SUA RESPOSTA. QUALQUER MUDANÇA PODE RESULTAR
# EM NOTA ZERO NA SUA AVALIAÇÃO.
# -----------------------------------------------------------------------------
a = leiaNumero('')
b = leiaNumero('')
c = leiaNumero('')
d = leiaNumero('')
escreva(media(a,b,c,d))
escreva(variacao(a,b,c,d))