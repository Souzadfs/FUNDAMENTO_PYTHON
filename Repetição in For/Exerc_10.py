#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Qual é o peso da {p}° pessoa? '))
    if p == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso

print(f'O maior peso digitado foi {maior}')
print(f'O menor peso digitado foi {menor}')