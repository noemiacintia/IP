# Calcular o valor de k, considerando que f,L,Q,ΔH,ϑ
# são dados de entrada e g=9.81 (gravidade) e ε=0.000002.

# D=8fLQ2π2gΔH−−−−−−−√5
# Rey=4QπDϑ
# k=0.25[log10(ε3.7D+5.74Rey0.9)]2

# ENTRADA:
# A entrada f,L,Q,ΔH,ϑ deve ser solicitada nesta ordem.
# Lembrando que g=9.81 e ε=0.000002  e π são constantes
# e NÃO devem ser pedidos como entradas.O valor de π
# deve ser utilizado como: math.pi (escreva assim
# mesmo, math.pi)

# SAÍDA:
# A saída deve apresentar o valor de D, Rey e k (com 4 casas decimais).

# Exemplo:
# Para a entrada:
# f = 0.2
# L = 50000
# Q = 0.65
# DeltaH = 22
# v = 0.000001

# A saída deve mostrar os dados a seguir (nesta ordem):
# D=1.7382
# Rey=476122.1893
# k=0.0132
# No entanto, você deve omitir variáveis e operadores na saída,
# exibindo apenas os números na ordem pedida, um valor por linha.
# Logo, a saída do seu programa para esse exemplo deve ser
# EXATAMENTE assim:
# 1.7382
# 476122.1893
# 0.0132

# DICA:
# O logaritmo na base 10 pode ser calculado com o comando:
# math.log10(expressao)
# Ex:
# math.log10(a*b)
# calcula o logaritmo na base 10 da expressão a*b.

# -*- coding: utf-8 -*-
import math
f = float(input())
L = float(input())
Q = float(input())
DeltaH = float(input())
v = float(input())

e = 0.000002
g = 9.81

D = ((8*f*L*(Q**2))/((math.pi**2)*(g)*DeltaH))**(1/5)
Rey = (4*Q)/(math.pi*D*v)
k = ((0.25)/(math.log10(((e)/(3.7*D))+(5.74/(Rey**0.9)))**2))

print("\n%.4f\n\n%.4f\n\n%.4f\n" % (D, Rey, k))