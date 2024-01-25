contatos = {}

print('Aqui você encontra os principais contatos de serviços de emergência.')
contatos = {"Polícia Militar": 190, "Serviço de Atendimento Móvel de Urgência" : 192, "Corpo de Bombeiros": 193, "Polícia Civil": 197, "Defesa Civil": 199}

nome_contato = input('Digite o nome do contato: ')

try:
    numero = contatos[nome_contato]
    print(f'O contato de {nome_contato} é {numero}')
          
except KeyError:
    print("Contato não encontrado")



