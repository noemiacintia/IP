# Escreva um programa em que, dadas duas datas fornecidas
# pelo usuário (uma de cada vez), mostre na tela a data mais
# recente. Cada data deve ser lida por partes: primeiro o dia,
# depois o mês e, por último, o ano (nesta ordem, cada leitura por vez).
# Perceba que serão, portanto, três leituras para cada uma das duas datas.
# Entrada: 
# Dia1, Mes1, Ano1, Dia2, Mes2 e Ano2 (nesta ordem, um de cada vez).
# Saída:
# Apenas uma das strings a seguir:
# 'DATA 1' (sem aspas e com um espaço antes do numeral), caso a primeira data lida seja a mais recente das duas; 
# 'DATA 2' (sem aspas e com um espaço antes do numeral), caso a segunda data lida seja a mais recente das duas;
# 'IGUAIS' (sem aspas), caso as duas datas sejam idênticas.

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