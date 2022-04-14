notas = [4, 9, 10, 5, 7]

contador = 0
notageral = 0


while contador < 5:
  notageral = notageral + notas[contador]
  contador = contador + 1

print("A média anual deste aluno é de: %.1f" % (notageral/5))
  

