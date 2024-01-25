nota = int (input('Informe uma nota de 0 a 10: '))
        
while nota > 10 or nota < 0: #enquanto
    nota = int (input('Valor inválido. Informe uma nota de 0 a 10: '))

if nota >= 7:
    print('Parabéns, você foi aprovado!')

else:
    print('Você foi reprovado.')


