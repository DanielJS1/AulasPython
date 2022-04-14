notas = [0, 0, 0, 0, 0]

c = 0
provas = 1

while c < 5:
  if provas == 5:
    notas[c] = float(input("Digite a nota da " + str(provas) + "° de prova(FINAL) do aluno:"))
  else:
    notas[c] = float(input("Digite a nota da " + str(provas) + "° prova do aluno:"))
  provas = provas + 1
  c = c + 1

contador = 0
notageral = 0


while contador < 5:
  notageral = notageral + notas[contador]
  contador = contador + 1

if (notageral/5) >= 6:
  print("APROVADO! A média anual deste aluno é de: %.1f" % (notageral/5))
else: 
  print("REPROVADO! A média anual deste aluno é de: %.1f" % (notageral/5))

