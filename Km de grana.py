dias=int(input('Quantos dias você usou esse carro?: '))
quilômetro=float(input('Quantos quilômetros você rodou?: '))
grana=(dias*60)+(quilômetro*0.15)
print(f'Você rodou {quilômetro}km, tendo o utilizado por {dias} dias, dando por fim uma dispesa de R${grana}.')
