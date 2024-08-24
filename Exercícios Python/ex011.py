#FAÇA UM PROGRAMA QUE LEIA A ALTURA E A LARGURA DE UMA PAREDE, CALCULE A SUA ÁREA, E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE, 1 LITRO DE TINTA PINTA UMA ÁREA DE 2M².

print('Quantidade de tinta necessária para pintura!')
altura = float(input('Digite a altura da parede: '))
largura = float(input(' Digite a largura da parede: '))
area = altura * largura
litros = area / 2

print(f'A área total da parede é de {area}M², para pintar essa área será necessário um total de {litros} litros de tinta!')