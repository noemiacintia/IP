'''0        n precisa ser positivo não-nulo
3           É PRIMO
4	        NÃO É PRIMO'''

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Lembre-se de que a correção será automatizada. Logo, é recomendado que, na 
# versão final do seu código (aquela que você deixará como resposta para 
# correção) você use inputs vazios, sem strings [ex: input()] e que os prints 
# na tela não façam nada mais do que o que o enunciado pede. Esteja atento para 
# não inserir pulos de linha adicionais, espaços em branco, ou qualquer outro 
# caractere não esperado. Também esteja atento com a ordem e formatos pedidos 
# nos enunciados para as entradas e saídas. Os enunciados são completos o 
# suficiente para que não fique nenhuma dúvida quanto às entradas e saídas. Os
# exemplos também são mostrados para que você perceba como seu programa deve se
# comportar como um todo (entradas,saídas e processamento). Desde a semana 4, 
# estamos alertando em vários meios (avisos, fóruns, aulas) que a falta de 
# atenção nesses aspectos pode resultar em nota zero ou notas muito baixas, 
# independente da lógica do algoritmo estar correta ou não. Não haverá revisão
# de nota para problemas causados por sua falta de atenção.
# -----------------------------------------------------------------------------


n = int(input())

while n<=0: 
    print('n precisa ser positivo não-nulo')
    n = int(input())
contaDiv=0 
div=1

while div<=n:
    if n%div==0:
        contaDiv=contaDiv+1
    div = div+1

if contaDiv==2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')
    