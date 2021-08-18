litros_de_gasolina = float(input("Informe quantos litros de gasolina foram abastecidos: "))

quilometros_andados = float(input("Informe quantos KM andou: "))

resultado = quilometros_andados/litros_de_gasolina # Aqui é float

#print("Voce anda " + str(resultado) + ' km por litro')
print("Voce anda",resultado,'km por litro')