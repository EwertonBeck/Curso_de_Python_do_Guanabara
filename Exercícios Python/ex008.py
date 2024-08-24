#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO EM METROS E CONVERTA PARA CENTÍMETROS E MILÍMETROS

print('Coversor de medidas!')
metro = float(input('Digite a medida em metros: '))
cm = metro * 100
mm = metro * 1000

print(f'{metro}M equivale a {cm} centímetros!')
print(f'{metro}M equivale a {mm} milímetros!')