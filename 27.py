from math import sqrt,floor 
# Importando somente 2 funções de math 

num = int (input ('Digite um numero: '))

raiz = sqrt (num)

print('A raiz de {} é igual a {:.2f}'.format (num,floor(raiz)) )