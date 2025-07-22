
palavra_secreta = 'perfume'
letra_acertada =''

while True:
    palavra = input('Digite uma letra: ')
    if len(palavra) > 1:
        print('Digite apenas uma letra')
        continue

    
    if palavra in palavra_secreta:
        letra_acertada += palavra
   
    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in palavra_secreta:
            palavra_formada += palavra_secreta

        else:
            palavra_secreta =+ '*'
        
        
        