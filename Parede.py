#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
#área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
#pinta uma área de 2m2.


parede_largura = float(input('Qual a largura de sua parede: '))
parede_altura = float(input('Qual a altura de sua parede: '))
area = (parede_altura * parede_largura) 
tinta = area / 2
print()
print(f'A área de sua parede é de {area}m2')
print(f'Será necessario {tinta} Litros de tinta.')