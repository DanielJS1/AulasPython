lista = [1,2,3,4,5]

n1 = int(input("Tente a sorte, escolha um número: "))

i = 0
j = 0
achou = False

while i < len(lista):
  if n1 == lista[i]:
    print("Parabéns! Você encontrou de primeira, %d estava na lista." % n1)
    achou = True
    i = i + 1
    break
  else:
    n2 = int(input("Ops, última tentativa, escolha outro número: "))
    while j < len(lista):
      if n2 == lista[j]:
        print("Parabéns! Antes tarde do que nunca, %d estava na lista." % n2)
        achou = True
      j = j + 1
    break

if achou == False:
  print("Não acertou em nenhuma das chances... Tente na próxima! Até maisss...")
else:
  print("Até mais sortudo.")
