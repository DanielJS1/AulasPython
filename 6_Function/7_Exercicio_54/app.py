def media(lista):
    medialista = 0
    soma = 0

    for n in lista:
        soma += n
        
    medialista = soma / len(lista)

    return medialista

lista = [10,12,12,34]

print(media(lista))

lista2 = [312,3122,2,222,2123,2,13,33]

print(media(lista2))