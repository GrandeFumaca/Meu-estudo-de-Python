casa=float(input('Largura da parede: '))
mansao=float(input('Altura da parede: '))
area=casa*mansao
tinta=area/2
print(f'Sua parede tem dimensão de {casa}x{mansao} e sua área é de {area:.2f}m^2.\nPara pintar essa parede para, você terá que terá que ter {tinta:.2f}lm')
