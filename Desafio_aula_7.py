#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO E MOSTRE O SEU SUCESSOR E SEU ANTECESSOR

valor = int(input('Digite um valor: '))
ant = int(valor - 1)
suc = int(valor + 1)

print(f'O antecessor de {valor} é {ant}, e seu sucessor é {suc}!')

# CRIE UM ALGORÍMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA

valor2 = int(input('Digite um valor: '))
dobro = int(valor2 * 2)
triplo = int(valor2 * 3)
rq = int(valor2 ** (1/2))

print(f'O dobro de {valor2} é {dobro}, o seu triplo é {triplo} e sua raiz quadrada é {rq}.')

# ESCREVA UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE A SUA MÉDIA

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
m = float( (n1 + n2) / 2)

print(f'O aluno ficou com a média {m}!')


#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO EM METROS E CONVERTA PARA CENTÍMETROS E MILÍMETROS

metro = float(input('Digite a medida em metros: '))
cm = float(metro * 100)
mm = float(metro * 1000)

print(f'{metro}M equivale a {cm} centímetros!')
print(f'{metro}M equivale a {mm} milímetros!')


# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO E EXIBA A SUA TABUADA

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

