'''Escreva um programa em que, dadas duas datas fornecidas
pelo usuário (uma de cada vez), mostre na tela a data mais
recente. Cada data deve ser lida por partes: primeiro o dia,
depois o mês e, por último, o ano (nesta ordem, cada leitura por vez).
Perceba que serão, portanto, três leituras para cada uma das duas datas.

Entrada: 
Dia1, Mes1, Ano1, Dia2, Mes2 e Ano2 (nesta ordem, um de cada vez).

Saída:
Apenas uma das strings a seguir:

'DATA 1' (sem aspas e com um espaço antes do numeral), caso a primeira data lida seja a mais recente das duas; 
'DATA 2' (sem aspas e com um espaço antes do numeral), caso a segunda data lida seja a mais recente das duas;
'IGUAIS' (sem aspas), caso as duas datas sejam idênticas.'''

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

dia1=int(input())
mes1=int(input())
ano1=int(input())
dia2=int(input())
mes2=int(input())
ano2=int(input())

if ano1>ano2 or (ano1==ano2 and (mes1>mes2 or (mes1==mes2 and dia1>dia2))):
    print('DATA 1')
elif ano1==ano2 and mes1==mes2 and dia1==dia2:
    print('IGUAIS')
else: 
    print('DATA 2')