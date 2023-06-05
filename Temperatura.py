#Escreva um programa que converta uma temperatura digitada em oC e converta para oF.
C = float(input('Entre com a Temperatura em Celcius: '))
f = (1.8 * C) + 32 
print(f'{C} Graus Celcius convertidos para fahrenheit = {f}F')