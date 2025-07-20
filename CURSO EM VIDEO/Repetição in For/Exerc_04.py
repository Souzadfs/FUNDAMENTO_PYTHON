#Exercício Python 04: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = float(input('Informe um numero: '))
valor = 0
for i in range(1, 11):
    print(f'{num:.0f} x {i} = {num * i}')