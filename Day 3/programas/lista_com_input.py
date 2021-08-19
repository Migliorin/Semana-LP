notas_lista = []

soma = 0 # nossa soma

for itr in range(4):
    nota = float(input("Escreva sua nota: "))
    soma = soma + nota # iterando uma soma

    notas_lista.append(nota)

resposta = soma/4
print('Nossa media',resposta)
print('Nossa ultima nota foi',notas_lista[3])

notas_lista[3] = 10

print('Nossa ultima nota foi',notas_lista[3])