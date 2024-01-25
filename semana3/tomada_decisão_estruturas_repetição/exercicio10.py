crescente = [] #cria lista

for numero in range (0,3): #a função range cria uma sequencia de numeros inteiros
    num = int (input ("Digite um valor: "))
    crescente.append (num)

crescente.sort () #ordena de forma crescente

print (f"Ordem crescente: {crescente}")


