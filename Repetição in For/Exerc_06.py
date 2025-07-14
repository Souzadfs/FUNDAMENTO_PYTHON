#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input("Primeiro termo: "))
Razao = int(input("Qual a razão: " ))
decimo = termo + (10 - 1) * Razao

for i in range(termo, decimo + Razao, Razao):
     print(i, end=' -> ')
