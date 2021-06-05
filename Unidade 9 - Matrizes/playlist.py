# Você agora é responsável por implementar algumas funcionalidades 
# para um serviço de playlist de músicas. Escreva um programa que 
# recebe um número inteiro n≥2, que indicará a quantidade de 
# músicas a serem lidas, e logo em seguida, o programa irá ler n 
# músicas juntamente com o seu tempo de duração. As músicas serão 
# fornecidas no seguinte formato:

# Nome_Da_Musica MM:SS

# onde MM:SS é o tempo de duração da música, exemplo: 01:30. 
# Assuma que o Nome_Da_Musica será sempre uma palavra única, 
# sem espaços. Assuma também que não existirão músicas com 
# duração idêntica nessa playlist.

# Seu programa deve mostrar, estritamente nesta ordem: 

# o nome da música de maior duração;
# o nome da música de menor duração;
# o tempo total de duração dessa playlist, no seguinte formato: H:MM:SS
# DICA: Para a resolução dessa questão, é recomendável a 
# utilização das funções datetime e timedelta da biblioteca datetime

 

# Entrada 
# O valor n (n≥2), e, em seguida, n entradas, uma por vez, 
# no formato: Nome_da_Musica MM:SS

 

# Saída
# Seu programa deve mostrar na saída os seguintes dados, 
# nesta ordem (ver exemplos):

# Nome da música de maior duração
# Nome da música de menor duração
# Tempo total de duração da playlist 
# (no formato especificado anteriormente)

# Exemplos

# Entrada	                    Saída
# 3
# Wonderwall 03:30
# Blackbird 05:30
# Colors 00:25                Blackbird
#                             Colors
#                             0:09:25


# 2
# Bellyache 00:10
# Once 00:15                  Once
#                             Bellyache
#                             0:00:25


# 2
# Asa_Branca 03:35
# Aviãozinho 03:26            Asa_Branca
#                             Aviãozinho
#                             0:07:01

# -*- coding: utf-8 -*-
from datetime import *

def maior_musica(musicas):
    # Faça aqui o codigo que mostra o nome da musica de maior duracao
    maiorTempo = timedelta(minutes=0, seconds=0)
    maiorNome = ""
    testando = timedelta(minutes=0, seconds=0)
    for i in range(len(musicas)):
        music = musicas[i].split(" ")
        nome = str(music[0])
        tempo = music[1]
        tempo = tempo.split(":")
        minutos = int(tempo[0])
        segundos = int(tempo[1])
        tempo = timedelta(minutes = minutos, seconds = segundos)
        t1 = tempo-maiorTempo 
        if t1>testando:
            maiorTempo = tempo
            maiorNome = nome
    return print(maiorNome)


def menor_musica(musicas):
    # Faça aqui o codigo que mostra o nome da musica de menor duracao
    maiorTempo = timedelta(minutes=0, seconds=0)
    menorNome = ""
    testando = timedelta(minutes=59, seconds=59)
    for i in range(len(musicas)):
        music = musicas[i].split(" ")
        nome = str(music[0])
        tempo = music[1]
        tempo = tempo.split(":")
        minutos = int(tempo[0])
        segundos = int(tempo[1])
        tempo = timedelta(minutes = minutos, seconds = segundos)
        t1 = tempo-maiorTempo 
        if t1<testando:
            testando = tempo
            menorNome = nome
    return print(menorNome) 


def soma_tempo_playlist(musicas):
    # Faça aqui o codigo que mostra o tempo de duracao total da playlist
    # Utilize o formato especificado no enunciado da questão
    tempoTotal = timedelta(minutes=0, seconds=0)
    testando = timedelta(minutes=0, seconds=0)
    for i in range(len(musicas)):
        music = musicas[i].split(" ")
        nome = str(music[0])
        tempo = music[1]
        tempo = tempo.split(":")
        minutos = int(tempo[0])
        segundos = int(tempo[1])
        tempo = timedelta(minutes = minutos, seconds = segundos)
        tempoTotal += tempo 
    return print(tempoTotal) 