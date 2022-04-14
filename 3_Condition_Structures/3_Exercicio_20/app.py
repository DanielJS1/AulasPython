nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))

if idade >= 18:
  print("Pode entrar na balada, %s." % nome)

else:
  print("Não pode entrar na balada, %s." % nome)
