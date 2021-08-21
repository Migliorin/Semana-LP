quantidade_de_info = int(input("Escreva quantos numeros serão informados: "))

lista_de_numeros = []

for iterador in range(quantidade_de_info):
    numero = float(input("Escreva seu numero: "))
    lista_de_numeros.append(numero)

print(lista_de_numeros)

lista_invertida = []

for iterador in range(len(lista_de_numeros),0,-1):
    nosso_index = iterador - 1
    valor_invertido = lista_de_numeros[nosso_index]
    lista_invertida.append(valor_invertido)

print(lista_invertida)

print('Comando para inverter',lista_de_numeros[::-1])

print('A lista se preserva',lista_de_numeros)


# [3.0, 2.0, 1.0], len é igual a 3

# [1.0, 2.0, 3.0]