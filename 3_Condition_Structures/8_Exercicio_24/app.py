n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

resultado = n1 * n2

if resultado <= 100:
  print("O resultado(%d) é baixo!" % resultado)
else:
  print("O resultado(%d) é alto!" % resultado)