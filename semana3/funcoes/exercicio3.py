def menu():
    opcao=int(input('Para converter Celsius para Fahrenheit digite 1. Para converter Fahrenheit para Celsius digite 2: '))
    if opcao == 1:
        fahrenheit()
    elif opcao == 2:
        celsius()
    else:
        print('Opção inválida.')

def fahrenheit():
    graus_celsius = float(input('Digite os graus Celsius: '))
    transf_fahr = (graus_celsius*1.8) + 32
    print(f'{graus_celsius:.2f} graus Celsius correspondem a {transf_fahr:.2f} graus Fahrenheit')

def celsius():
    graus_fahrenheit = float(input('Digite os graus Fahrenheit: '))
    transf_cels = (graus_fahrenheit - 32) / 1.8
    print(f'{graus_fahrenheit:.2f} graus Fahrenheit correspondem a {transf_cels:.2f} graus Celsius')

menu()







