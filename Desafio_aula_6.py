#crie um programa que leia dois mumeros e mostre a soma entre eles

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número'))
s = n1 + n2
print(f'A soma entre {n1} e {n2} é {s}')

# CRIE UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE TODAS AS INFORÇÕES SOBRE ELE

dado = input('Digite algo: ')
print(dado.isalnum())
print(dado.isalpha())
print(dado.islower())
print(dado.isnumeric())
print(dado.isupper())