print('ESTE É UM PROGRAMA USADO PARA CALCULAR AS NOTAS E SABER SE OS ALUNOES ESTÃO APROVADOS.')

aluno = input('Aluno: ')
n1 = float(input('Digite a nota do primeiro bimestre:'))
n2 = float(input('Digite a nota do segundo bimestre: '))
n3 = float(input('Digite a nota do terveiro bimestre: '))
n4 = float(input('Digite a nota do quarto bimestre: '))
media = (n1 + n2 + n3 + n4)/4

if media >= 7.0:
    print(f'A média do {aluno} foi {media}, e ele está aprovado!')
    print('Parabéns!')
if media == 6:
    print(f'A média do {aluno} foi {media}, e ele está em recuperação!')
if media < 6:
    print(f'A média do {aluno} foi {media}, e ele está reprovado!')