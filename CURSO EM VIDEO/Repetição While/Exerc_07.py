

termo = int(input('Quanto termo você quer mostrar: '))
t1 = 0
t2 = 1
cont = 3

while cont <= termo:
    t3 = t1 + t2
    print(f'{t3}', end= ' - ')
    t1 = t2
    t2 = t3
    cont += 1
    


