sucarilhos=str(input('Digite seu nome completo: '))
alto=sucarilhos.upper()
pequeno=sucarilhos.lower()
total_de_letras=len(sucarilhos)-sucarilhos.count(' ')
primeiro=len(sucarilhos.split()[0])
primeirasso=sucarilhos.split()[0]
print(f'"A minha alma tá armada, e apontada para a cara do sujeito."\n                                                        - Mameluco\nOlá {primeirasso}! Então, vou analisar seu nome:\nSeu nome em CapsLook é {alto}.\nSeu nome em literal mindinho é {pequeno}.\nO número total de letras no nome são de {total_de_letras}.\nO número total de letras no primeiro nome é {primeiro}.')
