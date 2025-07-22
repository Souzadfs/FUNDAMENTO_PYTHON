# While

senha_salva = "123456"
senha_digitada = ''
repeticao = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha repetidas em ({repeticao}x): ')
    

    repeticao += 1
    if repeticao > 2:
        print(f'Sua senha foi broqueada após {repeticao} tentativa')
        break

    if senha_salva == senha_digitada:
        print("Logado com Sucesso")
#print("Logado com Sucesso")