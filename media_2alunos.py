#. Desenvolva um programa que leia as duas notas de um aluno e mostre a sua média.
nome_aluno = input('Entre com o nome do aluno: ')
nota_1 = float(input('Entre com a primeira nota do aluno: '))
nota_2 = float(input('Entre com a segunda nota do aluno: '))
media = (nota_1 + nota_2)/2 

print(f'Média do aluno {nome_aluno} = {media}')