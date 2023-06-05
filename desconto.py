# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de
#desconto.

produto = (input('Entre com o nome do produto: '))
valor_produto = float(input('Entre com o valor do produto: R$'))
desconto = (valor_produto * 5 ) / 100
print()
print(f'Valor do {produto} sem desconto = R${valor_produto}')
print(f'Valor do desconto R${desconto}')
print(f'Valor do {produto} com desconto = R${valor_produto - desconto}')