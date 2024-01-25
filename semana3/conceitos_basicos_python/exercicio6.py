print('Olá, compare o tempo de viagem em diferentes meios de transposte.')
km = int(input('Informe qual a distância, em km, do seu destino: '))

horas_aviao = km/600
horas_carro = km/100
horas_onibus = km/80

minutos_aviao= ((km%600)/600)*60
minutos_carro = ((km%100)/100)*60
minutos_onibus = ((km%80)/80)*60

print(f'O tempo de viagem utilizando um avião é de {horas_aviao:.0f} horas e {minutos_aviao:.0f} minutos')
print(f'O tempo de viagem utilizando um carro é de {horas_carro:.0f} horas e {minutos_carro:.0f} minutos')
print(f'O tempo de viagem utilizando um ônibus é de {horas_onibus:.0f} horas e {minutos_onibus:.0f} minutos')


