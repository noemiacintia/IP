# Pablo começou a estudar matrizes e foi lhe dada a seguinte tarefa: 
# ele deverá criar um programa que construa uma Matriz(m,n) 
# estritamente de números inteiros.

# Caso o usuário do programa digite uma entrada que não seja um número 
# inteiro, ele deverá retornar a seguinte mensagem ao usuário: 
# "Erro: Você deve digitar apenas números inteiros."  (sem as aspas), e, 
# em seguida, pedir para ele tentar novamente. Enquanto o usuário não 
# digitar um número inteiro, o programa deve insistir com a mensagem de 
# erro, sempre pedindo na sequência para ele tentar novamente.

# As duas primeiras entradas do programa devem ser os valores inteiros m 
# (número de linhas) e n (número de colunas). O programa precisa, além 
# de permitir apenas números inteiros para essas entradas, assegurar que 
# cada um desses dois inteiros digitados sejam positivos não-nulos. Se o 
# número for inteiro, mas não atender essa exigência, no caso de m e n, o 
# programa deve exibir a mensagem: "Erro: Esse valor precisa ser positivo 
# e não-nulo." (sem as aspas), e, em seguida, pedir para ele tentar 
# novamente. Logo, por exemplo, se assim que o valor de m for digitado, 
# ele não estiver válido conforme as regras aqui especificadas, o 
# programa deve insistir exibindo a mensagem de erro apropriada e pedindo 
# que o usuário tente digitar novamente o valor para m até que o valor 
# digitado seja válido. O comportamento do programa deve ser semelhante para 
# a leitura de n.

# As demais m×n entradas serão os valores inteiros da Matriz(m,n). Cada 
# entrada deve ser validada imediatamente, retornando erro, se houver, e 
# pedindo para o usuário repetir a digitação da entrada.

# Por fim, uma última entrada do programa deverá ser um valor inteiro L 
# indicando uma das linhas da matriz. Note que o valor lido para L não é um 
# índice da matriz, mas, sim, o número de uma linha. Ou seja, começa em 1. 
# Seu programa deve verificar se o índice que corresponde à linha informada 
# existe na matriz lida. Se não existir, o programa deve retornar a seguinte 
# mensagem ao usuário: "Erro: A matriz informada não possui a linha L, pois 
# ela possui apenas X linhas." (sem as aspas e, trocando as letras L e X 
# pelos respectivos valores), e, em seguida, pedir para ele tentar novamente. 
# Isso deve se repetir até que o valor digitado para L seja válido. O 
# programa então finaliza exibindo o valor da soma dos elementos da linha L 
# informada.

# Dica 1: use tratamento de exceções nas validações

# Dica 2: crie uma função que realize a validação necessária para que o valor 
# digitado pelo usuário seja um número inteiro e crie uma outra função para 
# tratar a validação do inteiro positivo não-nulo.

# Entrada 
# m, n, os m×n valores inteiros que serão elementos da matriz, e L (cada entrada por vez)

# LEMBRE-SE: O programa só avança para a próxima entrada após ler um valor válido na leitura atual.

# Saída
# As eventuais mensagens de erro de validação, conforme o enunciado estabelece, quando houver. Uma em cada linha.

# O valor inteiro que represente a soma dos elementos da linha L válida.

# Exemplos

# Entrada	                                                Saída
# 2
# 2
# 0
# 1
# 2
# 3
# 1                                                          1



# a
# -1
# 2
# -2
# b
# 2
# 2
# 3
# 4
# a
# 4
# 9
# 2                                                       Erro: Você deve digitar apenas números inteiros.
#                                                         Erro: Esse valor precisa ser positivo e não-nulo.
#                                                         Erro: Esse valor precisa ser positivo e não-nulo.
#                                                         Erro: Você deve digitar apenas números inteiros.
#                                                         Erro: Você deve digitar apenas números inteiros.
#                                                         Erro: A matriz informada não possui a linha 9, pois ela possui apenas 2 linhas.
#                                                         8


# 2
# 2
# 3
# 4
# 5
# 6
# 3
# 4
# 1                                                       A matriz informada não possui a linha 3, pois ela possui apenas 2 linhas.
#                                                         A matriz informada não possui a linha 4, pois ela possui apenas 2 linhas.
#                                                         7


# 0
# a
# -1
# 2
# 2
# a
# 3
# 4
# 5
# 6
# -10
# 2                                                      Erro: Esse valor precisa ser positivo e não-nulo.
#                                                        Erro: Você deve digitar apenas números inteiros.
#                                                        Erro: Esse valor precisa ser positivo e não-nulo.
#                                                        Erro: Você deve digitar apenas números inteiros.
#                                                        Erro: A matriz informada não possui a linha -10, pois ela possui apenas 2 linhas.
#                                                        11 

# -*- coding: utf-8 -*-
while True:
    try:
        lin = int(input())
        if lin<=0:
            print('Erro: Esse valor precisa ser positivo e não-nulo.')
        else:
            break
    except ValueError:
        print('Erro: Você deve digitar apenas números inteiros.')
        
while True:
    try:
        col = int(input())
        if col<=0:
            print('Erro: Esse valor precisa ser positivo e não-nulo.')
        else:
            break
    except ValueError:
        print('Erro: Você deve digitar apenas números inteiros.')

matriz = []

for i in range(lin):
    matriz.append([])
    for j in range(col):
        aux = 0
        while True:
            try:
                aux = int(input())
                break
            except ValueError:
                print('Erro: Você deve digitar apenas números inteiros.')
        matriz[i].append(aux)
while True:
    L = int(input())
    if L>lin or L<=0:
        print('Erro: A matriz informada não possui a linha %d,'
        ' pois ela possui apenas %d linhas.' % (L, lin))
    else:
        print(sum(matriz[L-1]))
        break