# Suponha que os valores x1,x2,x3,x4,x5,x6,x7,x8,x9 representam 
# a imagem de um jogo da velha finalizado (com um único ou 
# nenhum vencedor, jogador 0 ou jogador 1), onde cada um dos 
# valores de x sejam formados apenas por 0s e 1s. Escreva um 
# programa em Python que peça ao usuário os 9 valores de x e 
# verifique o resultado da partida (0 venceu, 1 venceu ou empate).

# x1|x2|x3
# x4|x5|x6
# x7|x8|x9

# O jogo tem um vencedor sempre que uma linha, coluna ou diagonal 
# for formada por todos os números iguais (todos 1s ou todos 0s). 
# Caso um vencedor seja encontrado, seu programa deve informar 
# quem venceu: 0 (caso tenha sido o jogador 0) ou 1 (caso tenha 
# sido o jogador 1). Do contrário, o retorno do programa deve ser 
# E, indicando empate. Logo, as únicas possíveis saídas do seu 
# programa devem ser: '0', '1' ou 'E' (sem aspas). Para qualquer 
# conjunto de entradas, uma única saída deverá ser mostrada.

# O programa principal já está pronto no arquivo "principal.py". 
# Sua missão é implementar, somente no arquivo "funcoes.py", as 
# seguintes funções utilizadas pelo programa principal para que 
# este funcione corretamente:

# função lerJogadas() --> lê o tabuleiro do jogo da velha com as 
# 9 posições e suas respectivas jogadas. Ao ver os exemplos de 
# entradas logo abaixo, você deve notar que o programa deve 
# pedir 3 entradas para ler todo o tabuleiro e suas respectivas 
# jogadas, de modo que cada entrada recebe 3 posições de uma 
# mesma linha do tabuleiro, no formato "x1|x2|x3" (sem aspas). 
# A função deve retornar uma matriz 3x3 contendo todas as jogadas 
# válidas lidas do usuário. Nos exemplos abaixo, verifique as 
# possíveis mensagens de erro que seu programa deve exibir caso 
# uma entrada não esteja no formato adequado, ou possua pelo menos 
# uma jogada inválida.
# função jogadaValida() --> verifica se uma única jogada, recebida 
# por parâmetro, é válida para uma das posições do tabuleiro. 
# Uma jogada válida precisa ser um número inteiro binário. Caso não 
# seja válida, seu programa deve alertar para o usuário digitar 
# novamente todo o conjunto de entradas da linha que está sendo 
# analisada, até que toda a linha seja válida.
# função verificaJogo(matriz) --> recebe uma matriz 3x3 preenchida 
# com todas as jogadas válidas, verifica se há empate ou um 
# vencedor, e então retorna: '0' (sem aspas, que denota: jogador 0 
# venceu), '1' (sem aspas, que denota: jogador 1 venceu) ou 'E' 
# (sem aspas, que denota: empatou).
  
# OBS 1: Você não deve editar o arquivo "principal.py". Qualquer 
# edição ocasionará nota ZERO. Edite apenas o arquivo "funcoes.py".

# OBS 2: Você não deve utilizar o módulo numpy, pois ele não está 
# instalado no servidor do AVA.

# DICA: Considere utilizar tratamento de strings e exceções.

# Exemplos

# Entrada	                    Saída
# 2|1|3
# 0|1|2
# 0|1|1
# 1|0|0
# 0|1|1                       Jogadas inválidas na(s) entrada(s): 1, 3
#                             Jogadas inválidas na(s) entrada(s): 3
#                             E


# 0|0|1
# 1|0|1
# 1|1|0                       0



# |0|0|0|
# 0|0|0
# 1|10
# 1|1|0
# 1|0|1                       Entrada inválida. Tabuleiro não reconhecido.
#                             Entrada inválida. Tabuleiro não reconhecido.
#                             0


# 1|0|1
# 1|1|0
# 1|0|0                       1



# 0|0|1
# 1|1|0
# 0|1|1                       E

def verificaJogo(matriz):
    E = True
    for i in range(3):
        soma = matriz[i][0]+matriz[i][1]+matriz[i][2]
        if soma == '000':
            E = False
            return 0
        elif soma == '111':
            E = False 
            return 1
        
    for i in range(3):
        soma = matriz[0][i]+matriz[1][i]+matriz[2][i]
        if soma == '000':
            E = False
            return 0
        elif soma == '111':
            E = False
            return 1

    diagonal1 = matriz[0][0]+matriz[1][1]+matriz[2][2]
    if diagonal1 == '000':
        E = False
        return 0
    elif diagonal1 == '111':
        E = False
        return 1
    
    diagonal2 = matriz[0][2]+matriz[1][1]+matriz[2][0]
    if diagonal2 == '000':
        E = False
        return 0
    elif diagonal2 == '111':
        E = False
        return 1
        
    if E:
        return 'E'
    
def checkLinha(linha):
    erros = ''
    for i in range(0, len(linha), 1):
        if linha[i] != '0' and linha[i] != '1':
            if i == 0:
                erros +=str(i+1)
            else:
                if erros == '':
                    erros += str(i+1)
                else:
                    erros += ','+str(i+1)
    return erros
    
    
    
def getLinha():
    while True:
        linha = input()
        linha = linha.split('|')
        if len(linha) == 3:
            if (checkLinha(linha) != ''):
                print('Jogadas inválidas nas(s) entrada(s):', checkLinha(linha))
            else:
                return linha
        else:
            print('Entrada inválida. Tabuleiro não reconhecido.')
            
            
            
def lerJogadas():
    matriz = []
    for i in range(0, 3, 1):
        matriz.append(getLinha())
    return matriz