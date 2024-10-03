# VIRIFICAR SE TRÊS SEGMENTOS DE RETAS FORMAM UM TRIANGULO

r1 = float(input('Qual o tamanho da primeira reta? '))
r2 = float(input('Qual o tamanho da segunda reta? '))
r3 = float(input('Qual o tamanho da terceira reta? '))
print('-='*40)

#descobrir qual é o maior
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('As tres retas formam um triângulo!')
else:
    print('Não é possivel formar um triângulo!') 