print('Olá, essa é uma calculadora do Índice de Massa Corporal (IMC)')
peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em metros: '))

imc = peso / (altura*altura)

print(f'Seu IMC é {imc:.2f}')

