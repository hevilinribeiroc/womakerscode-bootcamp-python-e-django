print('Vamos classificar triângulos?')

ladoA = float(input('Informe o comprimento do lado A do triângulo: '))
ladoB = float(input('Informe o comprimento do lado B do triângulo: '))
ladoC = float(input('Informe o comprimento do lado C do triângulo: '))

if ladoA + ladoC < ladoB or ladoA + ladoB < ladoC or ladoB + ladoC < ladoA:
    print('Não é possível formar um triângulo com essas medidas.')

elif ladoA == ladoB and ladoB == ladoC:
    print('Essas medidas formam um triângulo equilátero, todos os lados são iguais.')

elif ladoA == ladoB or ladoB == ladoC or ladoC == ladoA:
    print('Essas medidas foram um triângulo isósceles, dois lados são iguais.')

else:
    print('Essas medidas formam um triângulo escaleno, todos os lados são diferentes.')
