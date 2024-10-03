# programa que leia o nome de uma cidade e diga se o nome começa com'santo'

cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[0:5] .upper() == 'SANTO')#verifica se os caracteres dos indices de 0 a 5 é igual a "Santo"
