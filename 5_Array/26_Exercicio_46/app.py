lista = [13, 55, 87, 12, 1333, 7, 434, 2]

menor_valor = lista[0]

for n in lista:
  if n < menor_valor:
    menor_valor = n

print(menor_valor)