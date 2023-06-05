#O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos
#dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem
#sorteada
from random import random,shuffle
def ordem():
    return random()
from random import * 
print('BEM VINDO AO SORTEIO DE APRESENTAÇÃO!')
nome1 = str(input('Digite o nome do 1o aluno: ')) 
nome2 = str(input('Digite o nome do 2o aluno: ')) 
nome3= str(input('Digite o nome do 3o aluno: ')) 
nome4 = str(input('Digite o nome do 4o aluno: ')) 
l1 = [nome1,nome2,nome3,nome4]
shuffle(l1,random)
print(f'A ordem de apresentação foi: {l1}')
