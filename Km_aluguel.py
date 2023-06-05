#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
#o carro custa R$60 por dia e R$0,15 por km rodado. ram

Nome_usuario = input('Qual o seu nome: ')
Km_percorrido = float(input('Entre com o KM já percorrido: '))
Dias_usado = int(input('Por quantos dias você usou o carro: ')) 
pagar_dias = Dias_usado * 60 
km_pagar = Km_percorrido * 0.15  
valor_total = pagar_dias + km_pagar 

print(f'O cliente {Nome_usuario}, percorreu por {Km_percorrido}Km, e por {Dias_usado} Dias.\nCom isso, o valor por dias usado é de R${pagar_dias}, e por KM rodado é de R${km_pagar}' )
print(f'O total a ser pago é de R${valor_total}')
