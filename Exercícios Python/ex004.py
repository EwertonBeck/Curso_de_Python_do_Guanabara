#FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES SOBRE ELE.

d = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(d))
print('Só tem espaços?', d.isspace())
print('É um número?', d.isnumeric())
print('É alfabético?', d.isalpha())
print('É alfanumérico?', d.isalnum())
print('Está em maiúsculas?', d.isupper())
print('Está em minúsculas?', d.islower())
print('Está capitalizada?', d.isidentifier())