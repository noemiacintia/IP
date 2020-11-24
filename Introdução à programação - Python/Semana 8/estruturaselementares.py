'''Escreva um programa em que dado um número real, calcule e mostre:

- a parte inteira do número
- a parte fracionária do número
  

Entrada: 
Um número real.

Saída:
A parte inteira e a parte fracionária do número lido (nesta ordem, uma linha para cada).'''

num = str(input())

parteInteira = ""
a = 0

for i in range(len(num)):
    if num[i]=="." :
        break
    else:
        parteInteira+=num[i]
    a+=1
print(int(parteInteira))

parteFracionaria = "0"

for i in range(a, len(num), 1):
    parteFracionaria+=num[i]
print(float(parteFracionaria))