print('Descubra o total de calorias queimadas em um mês')

horas_exercicio = float(input('Informe a quantidade de horas de exercício físico que você faz por semana: '))

minutos_exercicio = horas_exercicio*60

calorias_semana = minutos_exercicio*5

calorias_mes = calorias_semana*4

print(f'Você queima {calorias_mes:.2f} calorias por mês.')

