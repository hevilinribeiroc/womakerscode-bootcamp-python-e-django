# Funções

**Definindo a função soma:**

    def soma(num1,num2):
        calculo = num1+num2

    print(f'O resultado da soma é: {calculo}')

*(num1,num2) são paramêtros, que podem ser reutilizados em várias funções, evitando a repetição.*

    num1 = int(input('Digite o primeiro numero: '))

    num2 = int(input('Digite o segundo numero: '))

    soma(num1,num2) 

## Tratamento de exceções

**Usamos try e except, por exemplo, é impossível dividir um número por 0 (exceção), então pedimos ao programa tentar dividir dois números e se der o erro ZeroDivisionError, podemos escrever uma mensagem ao usuário sobre o erro.**

    def divisao (a,b):
        try:
            resultado = a/b
            print (resultado)
    
        except ZeroDivisionError as e:
            print(f'Erro: Operação Impossível. Detalhes {e}')

*as e* permite trazer mais detalhes do erro.

## Manipulação de arquivos

Vamos supor que tenhamos um arquivo chamado:

    file = 'arquivo.txt'


Abertura do arquivo para escrever:

    arquivo_escrita = open (file, "w")
    arquivo_escrita.write("Texto a ser  escrito")
    arquivo_escrita.close()

Abertura do arquivo somente para ler:

    arquivo_leitura = open (file, "r")
    leitura = arquivo_leitura.read()
    print(leitura)
    arquivo_leitura.close()

Abertura de arquivos binários:

    arquivo_binario = open (file, "wb")
    
