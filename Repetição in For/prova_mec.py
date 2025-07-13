pesos = [0.3226, 0.3226 ,0.3226, 0.3226,0.3226,0.5376, 0.5376 ,0.5376,0.3226 ,0.5376
,0.5376
,0.3226
,0.3226
,0.5376
,0.5376
,0.3226
,0.7527
,0.5376
,0.5376
,0.7527
,0.7527

]  # Pesos das 21 questões
nota_total = 0
peso_total = sum(pesos)

for i in range(21):
    while True:
        correta = input(f'A questão {i+1} está correta? (s/n): ').strip().lower()
        if correta in ['s', 'n']:
            break
        else:
            print("Digite apenas 's' para sim ou 'n' para não.")

    if correta == 's':
        print(f'Questão {i+1}: Correta! (+{pesos[i]} pontos)')
        nota_total += pesos[i]
    else:
        print(f'Questão {i+1}: Errada. (0 pontos)')

nota_final = (nota_total / peso_total) * 10
print(f'\nNota final: {nota_final:.2f}')
