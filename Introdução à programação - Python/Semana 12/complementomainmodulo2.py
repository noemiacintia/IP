# -*- coding: utf-8 -*-
from modulo2 import *
from datetime import *

musicas = []
# CONTINUE ...

while True:
    n = int(input())
    if n>=2:
        break

for i in range(n):
    musicas.append(str(input()))

# NÃO MEXA NAS LINHAS ABAIXO. VOCÊ DEVE IMPLEMENTAR AS FUNÇÕES, CONFORME O 
# ENUNCIADO, APENAS NO ARQUIVO funcoes.py
maior_musica(musicas)
menor_musica(musicas)
soma_tempo_playlist(musicas)
# NÃO ESQUEÇA DE TESTAR SEU CÓDIGO ANTES DE FINALIZAR O ENVIO 
# CÓDIGO QUE NÃO RODAR RECEBE NOTA ZERO