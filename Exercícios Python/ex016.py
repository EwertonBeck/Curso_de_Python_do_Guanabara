#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL E MOSTRE A SUA PORÇÃO INTEITA

import math

num = float(input('Digite um númeto real: '))
inteira = math.trunc(num)
print(f'A porção intera de {num} é {inteira}.')

from math import trunc

num2 = float(input('Digite um número real: '))
por_int = trunc(num2)
print(f'A parte inteira de {num2} é {por_int}!')