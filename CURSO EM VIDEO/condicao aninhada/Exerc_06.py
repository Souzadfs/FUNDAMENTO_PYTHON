from datetime import date
ano_atual = date.today().year

nasc = int(input(" Qual o seu ano de nascimento? "))

idade = ano_atual - nasc

if idade <= 9:
    print(f'Você nasceu em {nasc} e Sua idade é {idade} anos')
    print('Sua categoria é MIRIM')

elif idade <= 14:
     print(f'Você nasceu em {nasc} e Sua idade é {idade} anos')
     print('Sua categoria é INFANTIL')

elif idade <= 19:
     print(f'Você nasceu em {nasc} e Sua idade é {idade} anos')
     print('Sua categoria é JUNIOR')

elif idade <= 25:
     print(f'Você nasceu em {nasc} e Sua idade é {idade} anos')
     print('Sua categoria é SENIOR')

else:
     print(f'Você nasceu em {nasc} e Sua idade é {idade} anos')
     print('Sua categoria é MASTER')
