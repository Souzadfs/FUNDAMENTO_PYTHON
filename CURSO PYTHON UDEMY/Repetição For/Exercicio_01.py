
palavra_secreta = 'perfume'
letra_acertada =''
tentativa = 0

while True:
    palavra = input('Digite uma letra: ')
    tentativa += 1

    if len(palavra) > 1:
        print('Digite apenas uma letra')
        continue

    
    if palavra in palavra_secreta:
        letra_acertada += palavra
   
    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letra_acertada:
            palavra_formada += letra

        else:
            palavra_formada += '*'
        
    print(f'A palavra formada é: {palavra_formada}')   

    if palavra_formada == palavra_secreta:
        print(palavra_formada)
        print(tentativa)
        letra_acertada =''
        tentativa = 0
