#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO A PESSOA TEM E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR//COTAÇÃO DO DÓLAR= 5,48

print('Coversor de moedas!')
dinheiro = float(input('Digite o valor que você tem: R$ '))
dolar = 3.27
convertido = dinheiro / dolar
print(f'Com R${dinheiro:.2f} vocÊ consegue comprar ${convertido:.2f}.')