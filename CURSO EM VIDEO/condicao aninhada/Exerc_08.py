peso = float(input(" Qual seu Peso? "))
altura = float(input(" Qual a sua altura? "))

imc = peso / (altura**2)

if imc < 18.5:
    print(f" Seu IMC é {imc:.2f} e você esta abaixo do peso")

elif imc < 24.9:
    print(f'Seu IMC é {imc:.2f} e seu peso é normal')

elif imc < 29.9:
    print(f' Seu IMC é {imc:.2f} e seu peso é sobrepeso')    

elif imc < 34.9:
    print(f'Seu IMC é {imc:.2f} e seu peso é OBESIDADE GRAU 1')

elif imc < 39.9:
    print(f'Seu IMC é {imc:.2f} e seu peso pe OBESIDADE GRAU 2' )

else:
    print(f'Seu IMC é {imc:.2f} e seu peso é ODESIDADE GRAU 3 (GRAVE)')



    