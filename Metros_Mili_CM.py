#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
# e milímetros.

Metros = float(input('Entre com o valor desejado em metros: '))
Cm = float(Metros * 100) 
mili = float(Metros * 1000)
print()
print('Valor em metros = ',Metros)
print('Valor em Centimetros = ',Cm)
print('Valor em Milimetros = ',mili)