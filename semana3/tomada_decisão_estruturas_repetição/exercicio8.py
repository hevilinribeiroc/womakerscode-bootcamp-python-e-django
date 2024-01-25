print('Descubra qual número é maior')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1>=num2 and num1>num3:
    maior_num = num1

elif num2>num1 and num2>=num3:
    maior_num = num2

elif num3>=num1 and num3>num2:
    maior_num = num3

else:
    maior_num = num1

print(f'Entre os números apresentados, o maior é o {maior_num:.2f}')