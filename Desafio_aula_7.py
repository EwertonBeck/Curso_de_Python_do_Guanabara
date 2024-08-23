#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO E MOSTRE O SEU SUCESSOR E SEU ANTECESSOR

print('sucessor e antecessor!')
valor = int(input('Digite um valor: '))
ant = int(valor - 1)
suc = int(valor + 1)

print(f'O antecessor de {valor} é {ant}, e seu sucessor é {suc}!')

# CRIE UM ALGORÍMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA

print('Dobro, triplo e raiz quadrada!')
valor2 = int(input('Digite um valor: '))
dobro = int(valor2 * 2)
triplo = int(valor2 * 3)
rq = int(valor2 ** (1/2))

print(f'O dobro de {valor2} é {dobro}, o seu triplo é {triplo} e sua raiz quadrada é {rq}.')

# ESCREVA UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE A SUA MÉDIA

print('Média das notas!')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
m = float( (n1 + n2) / 2)

print(f'O aluno ficou com a média {m}!')


#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO EM METROS E CONVERTA PARA CENTÍMETROS E MILÍMETROS

print('Coversor de medidas!')
metro = float(input('Digite a medida em metros: '))
cm = float(metro * 100)
mm = float(metro * 1000)

print(f'{metro}M equivale a {cm} centímetros!')
print(f'{metro}M equivale a {mm} milímetros!')


# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO E EXIBA A SUA TABUADA

print('Tabuada!')
n = int(input('Qual tabuada você quer que eu faça? '))

print(f'{n} x 0 = {n*0}')
print(f'{n} x 1 = {n*1}')
print(f'{n} x 2 = {n*2}')
print(f'{n} x 3 = {n*3}')
print(f'{n} x 4 = {n*4}')
print(f'{n} x 5 = {n*5}')
print(f'{n} x 6 = {n*6}')
print(f'{n} x 7 = {n*7}')
print(f'{n} x 8 = {n*8}')
print(f'{n} x 9 = {n*9}')
print(f'{n} x 10 = {n*10}')

#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO A PESSOA TEM E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR//COTAÇÃO DO DÓLAR= 5,48

print('Coversor de moedas!')
dinheiro = float(input('Digite o valor que você tem: '))
dolar = float(5.48)
convertido = float(dinheiro / dolar)
print(f'Com R${dinheiro} vocÊ consegue comprar ${convertido}.')

#FAÇA UM PROGRAMA QUE LEIA A ALTURA E A LARGURA DE UMA PAREDE, CALCULE A SUA ÁREA, E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE, 1 LITRO DE TINTA PINTA UMA ÁREA DE 2M².

print('Quantidade de tinta necessária para pintura!')
altura = float(input('Digite a altura da parede: '))
largura = float(input(' Digite a largura da parede: '))
area = float(altura * largura)
litros = float(area / 2)

print(f'A área total da parede é de {area:.3}, para pintar essa área será necessário um total de {litros:.3} litros de tinta!')


# FAÇA UM ALGORÍTIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE O SEU NOVO PREÇO COM 5% DE DESCONTO

print('Desconto de 5%!')
preço = float(input('Digite o preço do produto: '))
desconto = float((preço * 5) / 100)
print(f'O produto teve um desconto de {desconto} Reais, seu valor ficou por {preço - desconto} Reais.')


# FAÇA UM ALGORÍTIMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE O SEU NOVO SALÁRIO COM 15% DE AUMENTO.

print('Aumento de salário!')
salario = float(input('Informe é o salário do colaborador:'))
aumento = float((salario*4) / 100)

print(f'O aumento real foi de R${aumento}.')
print(f'O novo salário do colaborador será de R${salario + aumento}')
