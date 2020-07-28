distancia=float(input('Qual é a distância da sua viagem?: '))
calculo_um=distancia*0.45
calculo_dois=distancia*0.50
if distancia>200.00:
    print(f'Estamos em promoção, como andou {distancia:.2f}pague apenas {calculo_um:.2f}R$.')
else:
    print(f'Você deve pagar {calculo_dois:.2f}R$.')
