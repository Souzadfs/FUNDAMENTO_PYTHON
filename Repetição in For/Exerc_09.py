#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today()

for i in range(1, 8):
    nasc = int(input('Qual seu ano de nascimento? '))
    
