ano=int(input('Digite um ano: '))
calculo_um=ano%4 and ano%400
if calculo_um==0:
    print('Este ano é BISSEXTO')
else:
    print('Este ano não é BISSEXTO')
