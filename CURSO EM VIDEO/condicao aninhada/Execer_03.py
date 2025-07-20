number_01 = int(input(" Primeiro numero: "))
number_02 = int(input(" Segundo numero: "))

if number_01 > number_02:
    print(f'O primeiro numero {number_01} é maior')

elif number_01 < number_02:
    print(f'O Segundo numero {number_02} é maior')

elif number_01 == number_02:
    print(f'Os numeros {number_01} e {number_02} são iguais')


else:
    print('Você não digitou um numero')          