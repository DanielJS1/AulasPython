camisa_1 = ["Verde", "libertadores", 299.90]
camisa_2 = ["Branca", "copa do brasil", 279.90]
camisa_3 = ["Bege", "supercopa", 399.90]

lista_camisas = [camisa_1, camisa_2, camisa_3]

print(lista_camisas)

for camisa in lista_camisas:
  print("A camisa é a %s e tem o pach da %s com o seu preço de: R$%.2f" % (camisa[0], camisa[1], camisa[2]))