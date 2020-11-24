'''Maria é uma bibliotecária e está entediada. Ela precisa de um programa 
que receba uma sequência de nomes de livros e/ou frases aleatórias, e que 
construa um pequeno texto com a maior palavra de cada entrada, na ordem em 
que foram inseridas numa sequência ou frase (caso tenham duas palavras de 
mesmo tamanho, a última, ou seja, a palavra mais à direita na frase, é a 
escolhida). A maior palavra é aquela que possui a maior quantidade de 
caracteres. Maria deseja que o programa continue recebendo entradas (novas 
frases ou sequências de caracteres) até que o usuário resolva digitar a 
seguinte frase: "terminei" (sem aspas e case-insensitive, ou seja, deve 
considerar qualquer combinação de letras maiúsculas e/ou minúsculas). 
Note que a frase "terminei" não é considerada para a produção da saída do 
programa. Além disso, caso o último caractere da maior palavra seja uma das 
seguintes vogais: a, e ou o, deve ser adicionada a letra “h” (sem aspas) 
ao final dessa palavra.

Você também deve saber que Maria tem problemas motores e, vez ou outra, 
acaba colocando ponto ou vírgula no começo e/ou final das palavras de 
forma aleatória e imprevisível. No entanto, Maria deseja que, caso ocorra, 
esses caracteres não devem contar no total de caracteres das palavras onde 
eles estiverem inseridos e caso essa palavra ainda assim seja a maior 
do nome do livro/frase, ela deve ir para o texto sem ponto e/ou sem a vírgula.
 
Por fim, precisamos considerar que a entrada do programa pode possuir letras 
maiúsculas e minúsculas sem qualquer respeito à norma padrão da Língua Portuguesa. 
Como seu programa produz um texto como saída, é importante que ele assegure que 
apenas a primeira palavra do texto produzido tem a primeira letra maiúscula. 
Todos os outros caracteres do texto produzido devem estar em minúsculo.

Maria está ansiosa pela sua implementação do pequeno programa que prestará grande ajuda a ela.


Entrada 
Sequência de nomes de livros e/ou frases aleatórias (uma por linha).

Saída
Um texto com a primeira letra maiúscula, formado seguindo estritamente as regras estabelecidas na descrição do problema.
 
Exemplos
Entrada	                                    Saída
.conTO de aia
maldicao de ALGO
eu terminEEEEei; as atividades
TERMINEI                                    Contoh maldicaoh termineeeeei


o ;celular quebrado
coracao de tinta;
amo neve.
terminei                                    Quebradoh coracaoh neveh


amo ;programar.
Guerra e .Paz;
Terminei                                    Programar guerrah'''



# -*- coding: utf-8 -*-

frase = []
while True:
    entrada = input()
    entrada = entrada.lower()
    excluirCaracter = ".,;"
    for char in excluirCaracter:
        entrada = entrada.replace(char, "")

    if entrada=='terminei':
        break
    else:
        maiorPalavra = ''
        entrada = entrada.split(' ')
        aux = len(entrada)
        
        for i in range(aux):
            maiorAux = len(maiorPalavra)
            aux2 = len(entrada[i])
            
            if aux2 > maiorAux:
                maiorPalavra = entrada[i]
    frase.append(maiorPalavra)
saida = ''

for i in range(len(frase)):
    if i==0:
        if frase[i][-1]=='a' or frase [i][-1] == 'e' or frase[i][-1]=='o' or frase[i][-1]=='u':
            saida+=frase[i]+'h'+' '
        else:
            saida+=frase[i]+' '
    else: 
        if frase[i][-1]=='a' or frase [i][-1] == 'e' or frase[i][-1]=='o':
            saida+=frase[i]+'h'+' '
        else:
            saida+=frase[i]+' '
saida = saida.strip()
print(saida.capitalize())