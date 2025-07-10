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

# Aplicar desconto
desconto = 0.10
desconto2 = 0.20

if escolha == '1':
    print('iphone')
    opcao_pgto = input('''Qual a forma de pagamento? 
                   [1] AVISTA
                   [2] PARCELADO
                       ''')
    if opcao_pgto == '1':
        preco_final = iphone * (1 - desconto)
        print(f"Você escolheu iPhone. Preço com 10% de desconto: R$ {preco_final:.2f}")
    elif opcao_pgto == '2':
        parc_x = input(''' Escolha a quantidade de parcelas
                       [1] Parcela
                       [2] Parcelas
                       [3] Parcelas
                       [4] Parcelas
                       Opção de parcelas: ''')
        if parc_x == '1' or parc_x == '2':
            print(f"Você escolheu iPhone. Preço é: R$ {iphone:.2f}")
        elif parc_x == '3':
            juros = iphone * (1 + desconto)
            parcelado = juros / 3 
            print(f'Você escolheu Iphone, e o valor parcelado em 3x, total a pagar R$ {juros:.2f} com 3 parcelas de R$ {parcelado:.2f}')
        elif parc_x == '4' :#or parc_x == '5':
            juros2 = iphone * (1 + desconto2)
            parc_4 = juros2 / 4
            print(f'Você escolheu Iphone, e o valor parcelado em 3x, total a pagar R$ {juros2:.2f} com 3 parcelas de R$ {parc_4:.2f}')
          




