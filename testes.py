#calculando a idade

nome = input('digite o seu nome: ')
ano_nasc = int(input('Digite o ano do seu nascimento: '))
ano_atual = int(input('Digite o ano em que estamos: '))
idade = ano_atual - ano_nasc

print(f'Olá {nome}, a sua idade é {idade} anos!')

if idade > 30:
    print('Você já viveu seus melhores anos!')
else:
    print('Você ainda é jovem!')