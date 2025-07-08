primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))

media = (primeira_nota + segunda_nota) / 2

if media < 5:
    print(f'reprovado {media}')

elif media < 6:
    print(f'Recuperação {media}')

elif media < 8:
    print(f'Aprovado {media}')

elif media > 8:
    print(f'Aprovado Parabens {media}')
  