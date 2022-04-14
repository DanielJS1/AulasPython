nome = input("Digite o seu nome: ")

if nome == "Iago":
  print("Olá, você é ZIKA!")
elif nome == "Daniel":
  print("Olá, você é FODA!!")
else:
  print("Você é um usuário comum!")


numero = int(input("Digite um número: "))

if numero > 0 and numero <= 5:
  print("Maior que 0")
elif numero > 5 and numero <= 10:
  print("Maior que 5")
elif numero > 10 and numero <= 20:
  print("Maior que 10")
elif numero > 20:
  print("Maior que 20")
else:
  print("Numero negativo")