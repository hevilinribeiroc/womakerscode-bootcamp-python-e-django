carteira = float(input('Digite quanto dinheiro você tem na carteira (reais): '))

conversao = {"Dólar americano": (carteira/4.91), "Peso argentino": carteira/0.02, "Dólar australiano": carteira/3.18, "Dólar canadense":carteira/3.64, "Franco suiço": carteira/0.42, "Euro": carteira/5.36, "Libra esterlina": carteira/6.21}

print('Com esse saldo, você poderia comprar:')
for moeda, valor in conversao.items():
    print("{}: {:.2f}".format(moeda, valor))