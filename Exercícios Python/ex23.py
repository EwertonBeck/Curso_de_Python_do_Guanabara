# FAZER UM PROGRMA QUE LEIA UM NUMERO DE QUATRO DIGITOS E MOSTRE CADA DIGITO SEPARADO

numero = int(input('Digite um número de quatro dígitos: '))

lista = numero.split()
print(f'Unidade: {lista[0][3]}')
print(f'Dezena: {lista[0][2]}')
print(f'Centena: {lista[0][1]}')
print(f'Milhar: {lista[0][0]}')