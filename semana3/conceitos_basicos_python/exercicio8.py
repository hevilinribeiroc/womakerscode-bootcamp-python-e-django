print('Essa é uma calculadora de salário')

valor_hora = float(input('Informe quanto você ganha por hora: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas no mês: '))

salario = valor_hora*horas_trabalhadas

print(f'Seu salário nesse mês foi de {salario:.2f} reais.')