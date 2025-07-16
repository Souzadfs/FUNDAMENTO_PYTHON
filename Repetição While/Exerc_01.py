#Exercício Python 01: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, 
# peça a digitação novamente até ter um valor correto.

genero = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]

while genero not in 'MmFf':
    genero = str(input('Dados invalidos: '))
print(f'O sexo digitado foi {genero}')