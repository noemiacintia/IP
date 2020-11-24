'''Crie uma função numeroPar que permita verificar se um dado número inteiro x,
passado como parâmetro, é um número par. O retorno da função deve ser do tipo bool.

A implementação do programa já está disponível para que você possa testar sua função.
  
Entrada: 
Já implementada.

 

Saída:
Já implementada.

 
Exemplos:

Entrada	        Saída
2               True

3               False

50              True'''

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# DEFINA SUA FUNÇÃO A SEGUIR
# -----------------------------------------------------------------------------
def numeroPar(x):
    if x%2==0:
        return True
    return False
# -----------------------------------------------------------------------------
# NÃO MEXER NAS PRÓXIMAS LINHAS. ELAS SERVEM PRA VOCÊ AVALIAR SUA FUNÇÃO
# -----------------------------------------------------------------------------
print(numeroPar(int(input())))