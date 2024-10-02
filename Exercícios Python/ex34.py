#CALCULE O AUMENTO DE SALÁRIO

sal = float(input('Digite o seu salário atual: '))

if sal >1250:
    print(f'O novo salário será de {sal+sal*10/100}')
else:
    print(f'O novo salário será de {sal+sal*15/100}')