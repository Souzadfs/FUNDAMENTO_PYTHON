termo = int(input("Primeiro termo: "))
Razao = int(input("Qual a razão: " ))
decimo = termo + (10 - 1) * Razao

for i in range(termo, decimo + Razao, Razao):
     print(i, end=' -> ')
