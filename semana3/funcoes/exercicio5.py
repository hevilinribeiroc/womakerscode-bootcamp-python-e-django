def contar_vogais(palavra):
    qnt = 0
    for letra in palavra:
        if letra == 'a' or letra=='e' or letra=='i' or letra =='o' or letra =='u':
            qnt += 1
    return qnt
        

palavra = input('Digite uma frase: ')
qnt = contar_vogais(palavra)
print(f'Essa frase possui {qnt} vogal(is).')

