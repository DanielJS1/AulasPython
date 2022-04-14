def retorna_lista_par(par):
    nova_lista = []

    for numero in par:
        if numero % 2 == 0:
            nova_lista.append(numero)
    
    return nova_lista

lista = [1,2,3,4,5,6,7,8,9,10]

lista_par = retorna_lista_par(lista)

print(lista_par)

lista2 = [31312,31,23,12,3213,21,32,13,21,3,1231,32132,13,12]

print(retorna_lista_par(lista2))