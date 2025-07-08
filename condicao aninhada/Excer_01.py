valor_casa = int(input("Qual valor da casa ?"))
Qual_salario = int(input("Qual seu salario ?"))
Qtd_prestcao = int(input(" Em quantas vezes você pretende pagar ?"))

prestacao = valor_casa / Qtd_prestcao
porcentagem = (30 / 100) * Qual_salario
qts_porcento = (porcentagem / Qual_salario) * 100

if prestacao < porcentagem:
    print('EMPRÉTISMO CONCEDIDO')
    print(f'O Valor da casa é {valor_casa}, a prestação será {prestacao:.2f},')
    print(porcentagem)
    print(f'{qts_porcento}%')

else:
    print('EMPRESTIMO NÃO CONCEDIDO')
    print(f'O valor da prestação {prestacao:.2f} excede os 30% do seu salario')