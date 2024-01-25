# Conceitos básicos de Python


## Imprimir uma mensagem na tela

    print('Olá mundo!')


## Tipos de variáveis

### INT (números inteiros)

    numero = int(input('Digite seu numero inteiro: '))

    print(numero)

### Tipo FLOAT (números decimais)
    
    numero1 = float(input('Digite seu numero float: '))
    
    print(numero1)

### Tipo STRING (texto)
    
    frase = input('Digite sua frase: ')
    
    print(frase)

## Operações Matemáticas:

* Subtração = -
* Multiplicação = *
* Divisão = /
* Divisão inteira = //
* Resto da divisao % *(por exemplo 10%3 = 1 (o resto da divisão é 1))*
* Soma = + 

*Confira um exemplo:*

    numero2 = int(input('Digite o numero 1: '))

    numero3 = int(input('Digite o numero 2: '))

    soma = numero1+numero2

    print(f'A soma dos números é {soma:.2f}') 

*Usamos .2f  para aparecer duas casas depois da vírgula*

*Para colocar variáveis dentro de um print utilizados {variável}*

## Incremento e Decremento
### Incremento += 
**Sua função é adicionar valor a uma variável**

    valor = 5

    valor +=1

    print(valor)

### Decremento -=
    valor1 = 5

    valor1 -=1**

    print(valor1)

## Ordem de precedência 

**É a ordem das operações, podemos definir prioridades utilizando parênteses**

    calculo = (2+5)*5

    print (calculo)

## Operadores relacionais:
* igual ==
* maior >
* menor >
* maior igual >=
* menor igual <=
* difente !=

