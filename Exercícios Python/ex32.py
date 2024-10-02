#ESCREVER UM PROGRAMA QUE ANALISE UM ANO E DIGA SE ELE É BISSESTO OU NÃO.

import calendar

ano = int(input('Digite o ano: '))
bissexto = calendar.isleap(ano)

if bissexto == True:
    print(f'O ano de {ano} é Bissexto!')
else:
    print(f'O ano de {ano} não é bissexto!')



