def moum(n):

  if n > 10:
    print("O %d é maior que 10." % n)
  elif n == 10:
    print("Oloco, dai 10 é igual a 10 po...")
  else:
    print("O %d é menor que 10." % n)

numero = int(input("Digite um número: "))

moum(numero)