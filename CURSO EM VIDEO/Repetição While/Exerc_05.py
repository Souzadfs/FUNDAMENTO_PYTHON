
primeiro = int(input("Primeiro termo: "))
Razao = int(input("Qual a razão: " ))

termo = primeiro
cont = 1

while  cont <= 10:
    termo += Razao
    cont += 1
    print(f'{termo}', end= ' - ')