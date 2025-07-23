#Exercício Python 03: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar

#[ 2 ] multiplicar

while True:
    primeiro_valor = float(input('Digite o primeiro valor :'))
    segundo_valor = float(input('Digite o segundo valor :'))
    print('''[ 1 ] Somar' 
             [ 2 ] Mutiplicar' 
             [ 3 ] Maior' 
             [ 4 ] Novo numero' 
             [ 5 ] Sair do Programa''')
    opcao = int(input ('>>>>>  Qual a sua opção? '))

    if opcao == 1:
       soma = primeiro_valor + segundo_valor
       print(soma)
        