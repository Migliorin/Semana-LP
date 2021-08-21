numero_participantes = int(input("Informe o numero de participantes: "))

dici_nomes = {}

for itr in range(numero_participantes):
    nome = input("Qual o nome para o participante " +  str(itr + 1 ) + ": ")
    idade = input("Qual a idade para o participante " + str(itr + 1)  + ": ")

    dici_nomes[nome] = idade

# a variavel muda de valor aqui, pois usamos para receber um novo valor
nome = input("Qual pessoa vc deseja saber a idade? : ")

print(dici_nomes[nome])