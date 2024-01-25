idade = int(input('Informe sua idade: '))

while idade < 0: 
    idade = int (input('Valor inválido. Informe sua idade: '))

if idade <= 11:
    print('Você é considerado(a) criança.')

elif idade >= 12 and idade <=17:
    print('Você é considerado(a) adolescente.')

elif idade >=18 and idade <=59:
    print('Você é considerado(a) adulto(a).')

else:
    print('Você é considerado(a) idoso(a).')

