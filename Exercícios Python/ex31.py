''''
print('VAMOS CALCULAR A SUA PASSAGEM!')

dis = float(input('Digite a distancia em Km da viagem: '))
valor1 = float(dis * 0.50)
valor2 = float(dis * 0.45)

if dis <= 200:
    print(f'O valor da sua pasagem será de R${valor1}!')
else:
    print(f'O valor da sua passagem será de R${valor2}!')
    '''

#correção do exercicio

distancia = float(input(' qual é a distancia da sua viagem? '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'O valor da sua viagem será de {preço:.2f}')
