n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite o valor: '))
    if n %2 == 0:
        par += 1
    else:
        impar += 1
print(f'A quantidade de número par é {par}, e de impar é {impar} ')
print('FIM')