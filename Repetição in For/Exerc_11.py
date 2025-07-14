#Exercício Python 11: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


mediaidade = 0
somaidade = 0
maioridadehomen = 0
nomevelho = ''

for i in range(1, 5):
    idade = int(input('Qual é a idade: '))
    nome = str(input('Qual nome: ')).strip()
    sexo = str(input('Qual Sexo? [M / F] ?  '))
    somaidade += idade

    if i == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
mediaidade = idade / 4
