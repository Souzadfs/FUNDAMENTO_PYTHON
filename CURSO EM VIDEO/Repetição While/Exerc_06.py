

primeiro = int(input("Primeiro termo: "))
Razao = int(input("Qual a razão: " ))


termo = primeiro
cont = 1
total = 0
quantidade = 10
while quantidade != 0:
    total += quantidade
    while  cont <= total:
        print(f'{termo}', end= ' - ')
        termo += Razao
        cont += 1
    print('PAUSA')

    quantidade = int(input('Quanto termo vc quer mostrar agora? '))
        