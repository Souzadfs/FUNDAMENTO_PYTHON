#Exercício Python 09: Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0

for i in range(1, 8):
    nasc = int(input('Qual seu ano de nascimento? '))
    idade = ano_atual -nasc
    
    if idade >= 21:
        print(f' {idade} Maior idade')
        totmaior += 1
        
    
    else:
        print(f' {idade} Menor idade')
        totmenor += 1

print(f'A quantidade de pessoa de Maior idade é {totmaior}')
print(f'A quantidade de pessoa de Menor idade é {totmenor}')