#UM PTOFESSOR QUE RSORTEAR UM DOS SEUS QUATRO ALINOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME ESCOLHIDO.
'''
import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terveiro aluno: ')
n4 = input('Digite o nome do Quarto aluno: ')
lista = [n1, n2, n3, n4]
sorteio = random.choice(lista)
print(f'O aluno sorteado foi: {sorteio}!')
'''
# Método simplificado 
from random import choice
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terveiro aluno: ')
n4 = input('Digite o nome do Quarto aluno: ')
lista = [n1, n2, n3, n4]
sorteio = choice(lista)
print(f'O aluno sorteado foi: {sorteio}!')