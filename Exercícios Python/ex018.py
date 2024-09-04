# LEIA UM ANGULO E MOSTRE SEU SENO, COSSENO E TANGENTE.
'''
import math

ang = int(input('Digite o ângulo: '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O ângulo digitado foi {ang}. \nSeu cosseno é {cos:.2f}. \nSeu seno é {sen:.2f}. \nSeu tangente é{tan:.2f}.')
'''

#Simplificado
from math import radians, sin, cos, tan

ang = int(input('Digite o ângulo: '))
cos = cos(radians(ang))
sen = sin(radians(ang))
tan = tan(radians(ang))
print(f'O ângulo digitado foi {ang}. \nSeu cosseno é {cos:.2f}. \nSeu seno é {sen:.2f}. \nSeu tangente é{tan:.2f}.')