cobaia=input('Digite algo: ')
print('O tipo desse valor é {}'.format(type(cobaia)))
print('Só tem espaço?: {}'.format(cobaia.isspace()))
print('É alfabético: {}'.format(cobaia.isnumeric()))
print('Contem números ou letras?: {}'.format(cobaia.isalnum()))
print('Contem apenas letras maiúsculas?: {}'.format(cobaia.isupper()))
print('Contem apenas letras minúsculas: {}'.format(cobaia.islower()))
