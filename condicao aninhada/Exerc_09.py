# Preços dos produtos
iphone = 9000
tv_60 = 4000
tablet = 2000

# Menu de escolha
escolha = input('''Olá! Posso ajudar? O que deseja comprar?
[1] iPhone
[2] TV 60"
[3] Tablet
Digite o número da opção: ''')

opcao_pgto = input('''Qual a forma de pagamento? 
                   [AVISTA]
                   [PARCELADO]''')

# Aplicar desconto de 10%
desconto = 0.10

if escolha == '1':
    opcao_pgto = input('''Qual a forma de pagamento? 
                   [AVISTA]
                   [PARCELADO]''')
    if opcao_pgto == 'AVISTA':
        preco_final = iphone * (1 - desconto)
        print(f"Você escolheu iPhone. Preço com 10% de desconto: R$ {preco_final:.2f}")





elif escolha == '2':
    preco_final = tv_60 * (1 - desconto)
    print(f"Você escolheu TV 60\". Preço com 10% de desconto: R$ {preco_final:.2f}")
elif escolha == '3':
    preco_final = tablet * (1 - desconto)
    print(f"Você escolheu Tablet. Preço com 10% de desconto: R$ {preco_final:.2f}")
else:
    print("Opção inválida.")
