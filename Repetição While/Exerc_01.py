#Exercício Python 01: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, 
# peça a digitação novamente até ter um valor correto.

genero = input('Qual seu sexo? [M/F] ')

while genero == 'M' or genero == 'F':
    if genero == 'M':
        print(f'Sexo {genero} registrado com sucesso! ')