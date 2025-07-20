#Exercício Python 07: Faça um programa que leia um 
# número inteiro e diga se ele é ou não um número primo.



num = int(input('Digite um número: '))
tot = 0

for i in range(1, num +1):
    if num % i == 0:
        print('\033[34m', end= '') #blue
        tot += 1
    else:
        print('\033[33m', end= '') #yellow
    print(i, end= ' ')

if tot == 2:
    print("Por isso é Primo")
else:
    print("ELe não é primo")


        
print(num, tot)