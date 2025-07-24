#Exercício Python 04: Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial


while True:
    numero = int(input('Digite um numero: '))
    f = factorial(numero)
    print(numero, f)

