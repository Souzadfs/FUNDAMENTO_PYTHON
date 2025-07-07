num = int(input('Digte um numero: '))
print(''' Escolha uma opção de base numerica
      [1] BINARIO
      [2] OCTAL
      [3] HEXADECIMAL''')
opcao = int(input('Escolha sua opção: '))

if opcao == 1:
    binario = bin(num)
    print(binario)

elif opcao == 2:
    octal = oct(num)
    print(octal)

elif opcao == 3:
    hexadecima = hex(num)
    print(hexadecima)

else:
    print('Valor invalido')