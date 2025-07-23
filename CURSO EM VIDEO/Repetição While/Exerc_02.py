#Exercício Python 02: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 1000)

while True:

    jogador = int(input('Eu sou o computador e pensei em um numero qual seu numero: '))


    if computador < jogador:
        print(f'É menos')
        print(computador)
    
    elif computador > jogador:
        print(f'Mais')

    elif computador == jogador:
        print(f'Acertou')
        break

print(computador)