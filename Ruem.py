carro=float(input('Qual a velocidade atual do carro? '))
calculo=(carro-80)*7
if carro>80:
    print(f'Puta vida, o normal era 80km/h seu arrombado, e não {carro}km/h. Toma uma multa de {calculo:.2f12}R$.')
else:
    print('Tá suave marreco.')
