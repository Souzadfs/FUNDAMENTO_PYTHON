# While

senha_salva = "123456"
senha_digitada = ''
repeticao = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha repetidas em {repeticao}x')

    repeticao =+ 1

print(repeticao)
print('Aquele laço a acima pode ter repetição infinita')