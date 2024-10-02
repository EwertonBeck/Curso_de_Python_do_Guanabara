# CRIAR UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE

#O NOME COM TODAS AS LETRA MAIUSCULAS

nome = str(input( 'Digite o nome completo: ')).strip()
print(f'Seu nome maiúsculo é {nome.upper()}')

# O NOME COM TADAS MINUSCULAS
print(f'Seu nome minucsculo é {nome.lower()}')

# QUANTAS LETRAS AO TODO SEM ESPAÇOS
print(f'Seu nome tem ao todo {len(nome)}')

# QUANTAS LETRAS O PRIMEIRO NOME 

dividido = nome.split()
print(dividido)
print(f'Seu primeiro nome tem {len(dividido[0])} letras')