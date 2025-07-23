#Exercício Python 03: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar

#[ 2 ] multiplicar

import os

primeiro_valor = float(input('Digite o primeiro valor : '))
segundo_valor = float(input('Digite o segundo valor : '))
opcao = 0

while opcao != 5:
    
    print('''    [ 1 ] Somar' 
    [ 2 ] Mutiplicar' 
    [ 3 ] Maior' 
    [ 4 ] Novo numero' 
    [ 5 ] Sair do Programa''')
    opcao = int(input ('>>>>>  Qual a sua opção? '))

    if opcao == 1:
       soma = primeiro_valor + segundo_valor
       print(f'A soma entre o {primeiro_valor} + {segundo_valor} = {soma}')

    elif opcao == 2:
        multiplicar = primeiro_valor * segundo_valor
        print(f'A Multiplicação entre {primeiro_valor} * {segundo_valor} = {multiplicar}')
    
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print(f'O Primeiro valor {primeiro_valor} é Maior que o {segundo_valor}') 
        elif primeiro_valor < segundo_valor:
            print(f'O Segundo valor {segundo_valor} é Maior que o {primeiro_valor}')
        else:
            print(f'Os valores entre {primeiro_valor} e {segundo_valor} são iguais')
    
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        primeiro_valor = float(input('Digite o primeiro valor : '))
        segundo_valor = float(input('Digite o segundo valor : '))

    elif opcao == 5:
        os.system('cls')
        print('Finalizado')
        break

    elif opcao != '12345':
        print(  'tente novamente')   