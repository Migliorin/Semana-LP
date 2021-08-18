litros_de_gasolina = float(input("Informe quantos litros de gasolina foram abastecidos: "))

quilometros_andados = float(input("Informe quantos KM andou: "))

resultado = quilometros_andados/litros_de_gasolina # Aqui é float


if(resultado > 20):
    print("carro de alto performance")


elif(resultado <= 20 and resultado > 10):
    print(resultado)
    print("carro de performance moderado")

elif(resultado == 11):
    print('ele entrou aqui')


else:
    print("carro de baixa performance")

print('qualquer coisa')