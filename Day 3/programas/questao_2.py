numero = int(input("Escreva um numero para calcular o fatorial: "))



resposta = 1

for valor in range(numero,0,-1):
    resposta = resposta * valor
    #print(valor)

print(resposta)


resposta = 1

valor = numero

while(valor >= 1):
    #print(valor)
    resposta = resposta * valor
    valor = valor - 1 

print('Nossa resposta e:', resposta)