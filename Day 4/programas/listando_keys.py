novo_dicionario =  {'Nome': 'Lucas',
                    'Idade': 20,
                    'Altura': 1.75}

nossas_chaves = novo_dicionario.keys()

#for chave in nossas_chaves:
#    print('Nossa chave e:',chave)
#    print('Nosso valor e:',novo_dicionario[chave])

dici = {}

for iterador in range(5):
    entrada = input("Escreva algo: ")
    dici[iterador] = entrada

print(dici)

