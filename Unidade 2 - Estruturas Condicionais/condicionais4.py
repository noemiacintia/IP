'''Suponha que você precise programar uma máquina de autoatendimento (ATM).
O usuário entrará com um valor inteiro (qualquer inteiro) correspondente ao
valor que deseja sacar, e a ATM precisa decidir como distribuir as cédulas
para o usuário. O programa deve sempre priorizar as cédulas de maior valor.
Considere que as únicas cédulas disponíveis são as de 20, 10, 5, 2 e 1.

ENTRADA:
Valor a ser sacado. Tem que ser inteiro.

SAÍDA:
Quantidade de cédulas de 20,10,5,2,1 (nesta ordem, cada quantidade em uma linha).

Ex.:
Suponha que um cliente queira sacar R$ 123.
A ATM deve fornecer 6 cédulas de 20,
0 de 10, 0 de 5, 1 de 2 e 1 de 1.

Logo, a entrada será:
123

E a saída do seu programa deve ser:
6
0
0
1
1

Apenas as quantidades devem ser mostradas, conforme mostrado acima.
DICA:
Teste com vários valores manualmente e no papel antes de
tentar desenvolver o seu algoritmo. Isso ajuda a pensar
na solução.'''

saque = int(input())

vinte = int(saque/20)
saque = saque % 20

dez = int(saque/10)
saque = saque % 10

cinco = int(saque/5)
saque = saque % 5

dois = int(saque/2)
saque = saque % 2

um = saque
    
print ('\n', vinte, '\n', dez, '\n', cinco, '\n', dois, '\n', um)