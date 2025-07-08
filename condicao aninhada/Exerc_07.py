r1 = int(input("Primeiro Segmento: "))
r2 = int(input("Segundo Segmento: "))
r3 = int(input("Terceiro Segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print("Os segmentos podem formar um TRIANGULO", end= '')
        print(" EQUILATERO ")

    elif r1 != r2 != r3 != r1:
        print(" Os Segmentos pode formar um TRIANGULO ", end= '')
        print(" ESCALENO ")

    else:
        print(" Os Segmentos podem formar um TRIANGULO ", end= '')
        print(" ISÓSCELES ")

else:
    print(" Os Segmentos não podem formar um TRIANGULO")
