#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.


primeiro = int(input("Primeiro termo: "))
Razao = int(input("Qual a razão: " ))

termo = primeiro
cont = 1

while  cont <= 10:
    termo += Razao
    cont += 1
    print(f'{termo}', end= ' - ')