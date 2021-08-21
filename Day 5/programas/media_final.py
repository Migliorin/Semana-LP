def calcula_media(nota_1,nota_2,nota_3):
    media_normal = (nota_1 + nota_2 + nota_3)/3

    if(media_normal >= 8):
        print("Voce foi aprovado, parabens")
    else:
        print('Voce foi de final')
        nota_final = float(input('Escreva sua nota final: '))
        media_final = (nota_final + (2*media_normal))/3
        if(media_final >= 6):
            print("Voce foi aprovado, parabens")
        else:
            print("Desculpe, mas voce nao passou :( ")


def pega_notas():
    notas = []
    for itr in range(3):
        nota = float(input("Escreva sua nota: "))
        notas.append(nota)
    return notas

notas = pega_notas()
calcula_media(notas[0],notas[1],notas[2])