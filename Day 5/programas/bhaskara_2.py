def bhaskara(a,b,c):
    discriminante = ((b**2) - (4*a*c))

    if(discriminante < 0):
        return False
    else:
        # Forma de tirar raiz usando operadores
        raiz = discriminante**(1/2)
        x1 = ((-b) + raiz)/(2*a)
        x2 = ((-b) - raiz)/(2*a)
        return [x1,x2]

resul = bhaskara(1,4,1)

if(resul == False):
    print("Nao ha raizes nos numeros reais")
else:
    # round() -> Arredondar nossos numeros
    x1 = round(resul[0],2)
    x2 = round(resul[1],2)

    print("Nossas raizes sao: " + str(x1) + " e " + str(x2))

