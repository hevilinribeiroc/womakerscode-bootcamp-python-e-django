print('Irei te fazer algumas perguntas relacionadas ao crime.')

perguntas = ["Telefonou para a vítima? ", "Esteve no local do crime? ", "Mora perto da vítima? ", "Devia para a vítima? ", "Já trabalhou com a vítima? "]

respostas = []
soma = 0

for pergunta in perguntas: 
    resposta = input (pergunta + "Digite sim ou não: ") 
    if resposta == "sim":
        soma += 1

respostas.append(resposta) 

classificacao_partipacao_crime = ["Inocente", "Suspeita", "Cúmplice", "Cúmplice","Assassina"]

if soma < 2:
    print(f'Eu te declaro {classificacao_partipacao_crime[0]}')

else:
    print(f'Eu te declaro {classificacao_partipacao_crime[soma-1]}')