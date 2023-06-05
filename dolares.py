# Crie um programa que leia quanto dinheiro uma pessoas tem na carteira e mostre quantos
#dólares ela pode comprar. Considere U$$1,00 = R$5,00.

Nome = input('Entre com seu nome: ')
Reais = float(input('Qual valor você possui em reais: '))
dolar = float(Reais / 5.00 )
print(f'O senhor {Nome} possui R${Reais}(Reais), e consegue comprar $${dolar}(Dolares)')