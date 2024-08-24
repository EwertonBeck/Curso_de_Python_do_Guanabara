# FAÇA UM ALGORÍTIMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE O SEU NOVO SALÁRIO COM 15% DE AUMENTO.

print('Aumento de salário!')
salario = float(input('Informe é o salário do colaborador:'))
aumento = salario*15/ 100

print(f'O aumento real foi de R${aumento}.')
print(f'O novo salário do colaborador será de R${salario + aumento}')