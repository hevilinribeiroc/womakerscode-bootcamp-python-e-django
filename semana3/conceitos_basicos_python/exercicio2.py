import datetime #importando módulo

currentDateTime = datetime.datetime.now() #data e hora atual
date = currentDateTime.date() #data atual
year = int(date.strftime("%Y")) #filtrando ano atual e convertendo para inteiro

print('Olá, essa é uma calculadora de idade, siga as instruções a seguir.')
ano_nascimento = int(input("Informe seu ano de nascimento: "))

idade_atual = year-ano_nascimento 

print(f'Atualmente você está com {idade_atual} anos.')