'''Suponha que Joãzinho quer que após cada venda de mercadoria, ele possa digitar o nome da pessoa que comprou, a quantidade e o produto em maiúsculo, minúsculo, misturado… do jeito que ele quiser. A entrada é dada em uma única linha na ordem: quantidade do produto, nome do produto, nome da pessoa. A saída esperada é o nome da pessoa em maiúsculo, um traço com espaço antes e depois para melhor visualização e em seguida a quantidade e o nome da mercadoria com a primeira letra maíuscula.
  

Entrada 
Quantidade do produto, nome do produto, nome da pessoa (nesta ordem, na mesma linha).

 

Saída
O nome da pessoa em maiúsculo, um traço com espaço antes e depois para melhor visualização e em seguida a quantidade e o nome da mercadoria com a primeira letra maíuscula tudo em uma mesma linha e na ordem descrita.

 
Exemplos

Entrada	                Saída
4 camisas pedro         PEDRO - 4 Camisas

9 TRuFAs lEANDro	    LEANDRO - 9 Trufas'''

# -*- coding: utf-8 -*-

compra = input()
compra = compra.split(' ')

quantidade = compra[0]
produto = compra[1].capitalize()
nomePessoa = compra[2].upper()

print(nomePessoa,'-',quantidade,produto)

