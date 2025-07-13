frase = str(input('Digite a Frase: ')).strip().upper()
palvras = frase.split()
junto = ''.join(palvras)

for i in range(len(junto) - 1, -1, -1):
    print(junto[i], end='')



    # print(f'A frase que você digitou é {frase}, {junto}, {palvras}')