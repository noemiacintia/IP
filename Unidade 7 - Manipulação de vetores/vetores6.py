#Escreva um programa em Python que dada uma matriz qualquer de tamanho m×n, devolve o resultado dessa matriz após ser rotacionada em 180º e espelhada.

# Exemplo: Para a matriz de entrada:

#     ⎡⎣⎢⎢510748856239⎤⎦⎥⎥

# A nova matriz a ser criada e devolvida como saída do programa deverá ser:
    
# ⎡⎣⎢⎢932658847015⎤⎦⎥⎥

  
# Entrada 
# As duas primeiras entradas são as dimensões da matriz: m (linhas) e n (colunas) nesta ordem, uma de cada vez. Em seguida, seu programa deve pedir as m×n entradas, uma de cada vez, de modo que cada uma corresponda a um elemento [i][j] da matriz, sendo a primeira para a posição [0][0], a segunda para posição [0][1] e assim por diante até [m−1][n−1].

 

# Saída
# A matriz resultante.

 
# Exemplos

# Entrada	            Saída
# 3
# 4
# 5
# 7
# 8
# 2
# 1
# 4
# 5
# 3
# 0
# 8
# 6
# 9                       [[9, 6, 8, 0], [3, 5, 4, 1], [2, 8, 7, 5]]


# 2
# 3
# 1
# 2
# 3
# 4
# 5
# 6                       [[6, 5, 4], [3, 2, 1]]


# 2
# 2
# 75
# 89
# 67
# 21                      [[21,67], [89,75]]

# -*- coding: utf-8 -*-
def reversa(lin):
    matrizReversa = []
    
    for i in range(len(lin)-1, -1, -1):
        matrizReversa.append(lin[i])
    return matrizReversa

def funNovaMatriz(matrizAntiga, lin, col):
    novaMatriz = []
    
    for i in range(0, lin, 1):
        matrizAntiga.append([])
        
        for j in range(0, col, 1):
            matrizAntiga[i].append(int(input()))
    
    for k in range(lin-1, -1, -1):
        novaMatriz.append(reversa(matrizAntiga[k]))
    return novaMatriz
    
lin = int(input())
col = int(input())
matrizAtual = []
saida = []

saida = funNovaMatriz(matrizAtual, lin, col)
print(saida)

