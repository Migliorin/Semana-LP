litros_de_gasolina = float(input("Informe quantos litros de gasolina foram abastecidos: "))

quilometros_andados = float(input("Informe quantos KM andou: "))

resultado = quilometros_andados/litros_de_gasolina # Aqui é float

if(resultado > 5):
    print("Meu resultado foi maior que 5:",resultado)
else:
    print("Ele nao atendeu nossa condicao")



# print(resultado)