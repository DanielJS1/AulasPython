def criar_escada(degraus):
  i = 1
  while i <= degraus:
    print("#" * i)
    i = i + 1

criar_escada(int(input("Digite a quantidade de degraus: ")))