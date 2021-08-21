def bhaskara(a,b,c):
    discriminante = ((b**2) - (4*a*c))

    if(discriminante < 0):
        print("Nao tem raiz nos numeros reais")
        return False
    elif(discriminante == 0):
        resultado = (-b)/(2*a)
        return resultado
    else:

        # Forma de tirar raiz usando operadores
        raiz = discriminante**(1/2)

        x1 = ((-b) + raiz)/(2*a)

        x2 = ((-b) - raiz)/(2*a)

        return [x1,x2]

print(bhaskara(9,1,1))