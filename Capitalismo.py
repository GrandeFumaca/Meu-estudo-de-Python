produto=float(input('Qual o valor do produto? R$ '))
desconto=int(input('Qual foi o desconto do produto: '))
calculo=(desconto/100)*produto
print(f'O valor do produto foi {produto:.2f}, que sofreu um desconto de {desconto}%, que por fim chegou no valor de R${calculo:.2f}')
