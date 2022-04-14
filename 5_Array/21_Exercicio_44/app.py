numeros = [11, 22, 33, 44, 55]

numero_a_localizar = int(input("Que número deseja buscar? "))

encontrado = False

for n in numeros:
  if n == numero_a_localizar:
    print("O número %d foi localizado!" % n)
    encontrado = True

if encontrado == False:
  print("O numero %d não foi localizado!" % numero_a_localizar)
  