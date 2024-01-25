#Cria um dicionário representando um catalogo que irá aparecer para o cliente
amostra_catalogo = {}
amostra_catalogo['1. Quincas Borba - Machado de Assis'] = 25.19
amostra_catalogo['2. Angústia - Glaciliano Ramos'] = 47.92
amostra_catalogo['3. Mensagem - Fernando Pessoa'] = 35.94
amostra_catalogo['4. Nós matamos o Cão Tinhoso - Luís Bernardo Honwana'] = 38.17
amostra_catalogo['5. Campo Geral - Guimarães Rosa'] = 39.76

#Cria um dicionário só com o código dos itens 
catalogo = {}
catalogo['1'] = 25.19
catalogo['2'] = 47.92
catalogo['3'] = 35.94
catalogo['4'] = 38.17
catalogo['5'] = 39.76

# Crie um dicionário vazio representando um carrinho de compras.
carrinho = {}

print(f'Olá, este é o Mundo da Leitura WMC. Confira nosso catálogo a seguir: {amostra_catalogo}')
item = input('Digite o código do item que você quer adicionar ao carrinho: ')

while item != "nao": #enquanto for diferente de na5o
    qnt = int(input('Digite a quantidade: ')) 
    if item in carrinho: #se o item já existir no carrinho
        carrinho[item]["quantidade"] += qnt #incrementa apenas a quantidade digitada pelo cliente
    else:
        carrinho[item] = {"quantidade": qnt, "preço": catalogo[item]} #cria outro dicionario com a qnt e valor.
    adicionar_mais = input('Deseja adicionar mais itens? Digite sim ou nao: ') 
    if adicionar_mais == 'sim': 
        item = input('Digite o código do item que você quer adicionar ao carrinho: ')
    else:
        item = "nao"

print('Carrinho: ')

#imprime os itens do carrinho
for item, dados in carrinho.items():
    nome = list(amostra_catalogo.keys())[int(item) - 1] #Cria uma lista com as chaves do amostra_catalogo e irá acessar a chave do nome do livroatravés da chave do item
    quantidade = dados["quantidade"] 
    preco = dados["preço"]
    print("%s: quantidade: %d, preço: %.2f" % (nome, quantidade, preco)) 

total = 0
for produto, preco in carrinho.items():
    total += preco["quantidade"] * float(preco["preço"]) 

print(f"Total do carrinho de compras: R$ {total:.2f}")







