#Exercício Python 04: Faça um programa que leia um número qualquer e mostre o seu fatorial.

#from math import factorial


#while True:
#    numero = int(input('Digite um numero: '))
#    f = factorial(numero)
#    print(numero, f)..


numero = int(input('Digite um numero: '))
c = numero
f = 1

while  c > 0:
    print(f'{c}', end=' ')
    print('x ' if c > 1 else '=', end=' ')
   
    f *= c
    c -= 1

print(f)