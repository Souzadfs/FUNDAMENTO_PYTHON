#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input('Digite a Frase: ')).strip().upper()
palvras = frase.split()
junto = ''.join(palvras)
inverso = ''

for i in range(len(junto) - 1, -1, -1):
    #print(junto[i], end='')
    inverso += junto[i]
   
if inverso == junto:
    print(f'Frase que vc digitou é um palindromo {junto},{inverso}')
    
else:
    print(f'Frase que vc digitou NÂO é um palindromo {junto},{inverso}')
      # print(f'A frase que você digitou é {frase}, {junto}, {palvras}')