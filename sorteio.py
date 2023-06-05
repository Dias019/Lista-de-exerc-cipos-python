#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
#programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
from random import * 
print('BEM VINDO AO SORTEIO DE ALUNOS!')
nome1 = str(input('Digite o nome do 1 aluno: ')) 
nome2 = str(input('Digite o nome do 2 aluno: ')) 
nome3= str(input('Digite o nome do 3 aluno: ')) 
nome4 = str(input('Digite o nome do 4 aluno: ')) 
l1 = [nome1,nome2,nome3,nome4]
print(f'O aluno sorteado foi: {choice(l1)}')