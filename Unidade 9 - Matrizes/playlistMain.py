# -*- coding: utf-8 -*-
from playlist import *
from datetime import *

musicas = []

while True:
    n = int(input())
    if n>=2:
        break

for i in range(n):
    musicas.append(str(input()))

maior_musica(musicas)
menor_musica(musicas)
soma_tempo_playlist(musicas)