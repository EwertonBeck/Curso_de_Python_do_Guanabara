#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL E MOSTRE A SUA PORÇÃO INTEITA

import math

num = float(input('Digite um númeto real: '))
inteira = math.trunc(num)
print(f'A porção intera de {num} é {inteira}.')


from math import trunc

num2 = float(input('Digite um número real: '))
por_int = trunc(num2)

print(f'O valor digitado foi {num2} e sua porção inteira é {por_int}!')
