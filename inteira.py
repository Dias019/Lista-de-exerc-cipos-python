#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua
#porção inteira. Exemplo: o número 6,127 tem a parte inteira 6 
import math
numero = float(input('Entre com um valor Real: '))
print(f'Valor inteiro do número informado = {math.trunc(numero)}')
