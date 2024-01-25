print('Vamos ver se sei qual o maior número?')

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))

if num1 > num2:
    print(f'O número {num1:.2f} é o maior')

elif num2 > num1:
     print(f'O número {num2:.2f} é o maior')

else: 
    print('Os dois números são iguais')