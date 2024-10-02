v = int(input('Digite a velocidade do veículo: '))
m = (v-80)*7

print('VocÊ está dentro da velocidade permitida!')
if v > 80:
    print('Você ultrapassou o limite de velocidade e foi multado!')
    print(f'O valor da multa é de R${m:.2f}!')