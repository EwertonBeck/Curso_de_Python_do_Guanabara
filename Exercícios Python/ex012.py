
# FAÇA UM ALGORÍTIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE O SEU NOVO PREÇO COM 5% DE DESCONTO

print('Desconto de 5%!')
preço = float(input('Digite o preço do produto: '))
desconto = preço * 5 / 100
print(f'O produto teve um desconto de {desconto:.2f} Reais, seu valor ficou por {preço - desconto:.2f} Reais.')