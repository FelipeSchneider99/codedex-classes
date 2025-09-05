pesos=(float(input('Enter amount in Pesos(COP): '))* 0.00025)
# 1 peso = 0.00025 dollars
soles=(float(input('Enter amount in Soles(PEN): '))* 0.28)
# 1 sol = 0.28 dollars
reais=(float(input('Enter amount in Reais(BRL): '))* 0.18)
# 1 real = 0.18 dollars
usd = pesos + soles + reais
print('Total in USD:', usd)