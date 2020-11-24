'''O principal prêmio da Olimpíada Brasileira de Informática é o
convite para os cursos de programação oferecidos no Instituto de 
Computação da Unicamp, com todas as despesas pagas pela Fundação 
Carlos Chagas, patrocinadora da OBI. São convidados apenas os 
competidores que atingem um certo número mínimo de pontos, 
consideradas as duas fases de provas. Você foi contratado pela 
Coordenação da OBI para fazer um programa que, dados os números 
de pontos obtidos por cada competidor em cada uma das fases, e o 
número mínimo de pontos para ser convidado, determine quantos 
competidores serão convidados para o curso na Unicamp. 
Você deve considerar que

- todos os competidores participaram das duas fases;
- o total de pontos de um competidor é a soma dos pontos obtidos nas duas fases.
Por exemplo, se a pontuação mínima para ser convidado é 435 pontos, um competidor
que tenha obtido 200 pontos na primeira fase e 235 pontos na segunda fase será 
convidado para o curso na Unicamp. Já um competidor que tenha obtido 200 pontos 
na primeira fase e 234 pontos na segunda fase não será convidado.


Entrada: 
A primeira entrada contém um número N e a segunda entrada contém um número P, 
representando, respectivamente, o número de competidores e o número mínimo de 
pontos para ser convidado. Cada uma das 2×N entradas seguintes contém dois 
números inteiros X e Y, de forma alternada, indicando a pontuação de um competidor 
em cada uma das fases, sendo X a pontuação do competidor na primeira fase e Y a 
pontuação do competidor na segunda fase.

Saída
Seu programa deve imprimir na saída padrão uma única linha contendo 
um único inteiro, indicando o número de competidores que serão convidados 
a participar do curso na Unicamp.

 

Exemplos
Entrada	            Saída
3
100
50
50
100
0
49
50                    2



4
235
100
134
0
0
200
200
150
150
                      2 '''

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
p = int(input())

cont=0

for i in range(0, n, 1):
    x = int(input())
    y = int(input())
    if x+y>=p:
        cont+=1
print(cont)