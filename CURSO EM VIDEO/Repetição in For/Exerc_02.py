#Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for n in range(0, 51):
    if n %2 == 1:
        print(n, end= ' ')