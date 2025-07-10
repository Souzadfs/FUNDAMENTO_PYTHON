from random import randint
itens = ('Papel', 'tesoura', 'Pedra')
computador = randint(1, 3)

jogador = int(input('''Papel, Tesoura, Pedra
                    [1] Papel
                    [2] Tesoura
                    [3] Pedra
                    Escolha uma opção: '''))
print('=-' * 11)
print(f'O Jogador jogou {itens[jogador]}')
print(f'O Computador jogou {itens[computador]}')
print('=-' * 11)

if computador == 1:
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador Venceu!')
    elif jogador == 3:
        print('JOgador Venceu!')

elif computador == 2:
    if jogador == 1:
        print('Computador Venceu!')
    elif jogador == 2:
        print('EMPATE!')
    elif jogador == 3:
        print('Jogador Venceu')

elif computador == 3:
    if jogador == 1:
        print('Jogador vence!')
    elif jogador == 2:
        print('Computador Venceu!')
    elif jogador == 3:
        print('EMPATE!')



