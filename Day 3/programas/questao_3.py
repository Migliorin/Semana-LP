flag = True

lista_de_numeros = [] # Lista onde sera armazenado nossos numeros

while(flag): # precisa ser true para executar
    numero = float(input("Informe o numero para ser armazenado: "))
    
    if(numero < 0):
        flag = False
    else:
        lista_de_numeros.append(numero) # adicionamos nosso numero no final da lista

print('Nossa lista:',lista_de_numeros)
