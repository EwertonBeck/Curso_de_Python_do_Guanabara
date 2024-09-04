# O PROFESSOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS, FAÇA UM PROGRAMA QUE LEIA OS NOMES DE 4 ALUNOD E MOSTRE A OREM SORTEADA
'''
import random
n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem será {lista}!')
'''
from random import shuffle
n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')

lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem será {lista}!')