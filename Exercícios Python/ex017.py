#FAÇA UM PROGRAMA QUE LEI O COMPRIMENT DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA!

import math
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente:'))
hipotenusa =math.hypot(oposto , adjacente) 
print(f'O comprimento da hipotenusa é {hipotenusa}')

from math import hypot
op = float(input('digite a medida do cateto oposto: '))
ad = float(input('Digite a medida do cateto adjacente: '))
hip = hypot(op , ad )
print(f'A hipotenusa é {hip}!')
