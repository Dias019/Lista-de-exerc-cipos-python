Nome_funcionario = input('Qual o seu nome: ')
salario_atual = float(input('Qual o seu sálario atualmente: '))
aumento = (salario_atual * 15 ) / 100
novo_salario = salario_atual + aumento

print(f'O salario de {Nome_funcionario}, é de R${salario_atual}, e teve um aumento de R${aumento}(15%), passando a ter um novo salario de R${novo_salario} ')