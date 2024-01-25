n_pares = 0
n_impares = 0
n = int(input('Insira um número inteiro (ou 0 para sair): '))

while n < 0: #enquanto for negativo, não inicia a contagem
    n=int(input('Erro. O número precisa ser positivo'))

while n != 0: #enquanto for diferente de zero, vai pedir os números e contar
    n = int(input('Insira um número inteiro: '))
    if n>0 and n%2 == 0:
        n_pares += 1
    else:
        n_impares += 1
    
print(f'Foram inseridos {n_pares} números pares e {n_impares} números ímpares')