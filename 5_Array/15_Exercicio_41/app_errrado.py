lista1 = []
lista2 = []

i = 0
n = 1

i2 = 0
n2 = 1

while i < 3:
  lista1.append(input("Digite 3 nomes de menino que você gostaria, o " + str(n) + "° sendo:"))
  n = n + 1
  i = i + 1

while i2 < 3:
  lista2.append(input("Digite 3 nomes de menina que você gostaria, o " + str(n2) + "° sendo:"))
  n2 = n2 + 1
  i2 = i2 + 1

nomes = lista1, lista2

print(nomes)
