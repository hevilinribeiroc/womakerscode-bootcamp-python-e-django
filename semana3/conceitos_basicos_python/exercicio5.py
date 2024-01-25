print('Olá, essa é uma calculadora simples de salário líquido')
salario_bruto = float(input('Digite seu salário bruto: '))

if salario_bruto <= 1903.98:
    aliquota = 0
    imposto = aliquota
    
elif 1903.99 <= salario_bruto <= 2826.65:
    aliquota = 7.5
    imposto = salario_bruto*(aliquota/100)

elif 2826.66 <= salario_bruto <= 3751.05:
    aliquota = 15
    imposto = salario_bruto*(aliquota/100)   

elif 3751.06 <= salario_bruto <= 4664.68:
    aliquota = 22.5
    imposto = salario_bruto*(aliquota/100)  

else:
    aliquota = 27.5
    imposto = salario_bruto*(aliquota/100)

salario_liquido = salario_bruto - imposto

print (f'Seu salário bruto é {salario_bruto:.2f} reais.')
print (f'O percentual de desconto correspondente a sua faixa de renda é {aliquota}%')
print (f'Seu salário liquído é {salario_liquido:.2f} reais.')