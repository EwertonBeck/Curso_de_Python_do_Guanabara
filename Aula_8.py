#importação de bibliotecas

import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {math.ceil(raiz)}')#usado o comando math para arredondar a raiz quadrada!

#AQUI FOI IMPORTADO APENAS A FUNÇÃO SQRT DA BIBLIOTECA, ALETRANDO TAMBEM O MODO COMO SE USA O METODO CEIL
from math import sqrt, ceil

num = int(input('Digite um numero: '))
raiz = sqrt(num)
print(f'A raiz quadrada de {num} é {ceil(raiz)}!')



