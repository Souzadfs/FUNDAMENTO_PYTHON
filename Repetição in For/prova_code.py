respostas = []
for i in range(1, 22):
    resposta = float(input(f'Questão {i}: '))
    respostas.append(resposta)

soma = sum(respostas)
print(f'Soma total: {soma}')
