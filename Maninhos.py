from random import shuffle
leponga=str(input('Digite o nome do primeiro aluno: '))
rian=str(input('Digite o nome do segundo aluno: '))
rodrigao=str(input('Digite o nome do terceiro aluno: '))
mojo=str(input('Digite o nome do quarto aluno: '))
vieira=[leponga, rian, rodrigao, mojo]
shuffle(vieira)
print(f'A apresentação vai ser: ')
print(vieira)
