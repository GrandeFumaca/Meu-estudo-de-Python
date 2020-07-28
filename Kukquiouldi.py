cuck=str(input('Digite uma frase: ')).lower()
contar=cuck.count('a')
esquerda=cuck.find('a')+1
direita=cuck.rfind('a')+1
print(f'Na sua frase, possui {contar} vezes a letra "a"\nA sua primeira letra "a" apareceu na posição {esquerda}\nA sua última letra "a" apareceu na posição {direita}')
