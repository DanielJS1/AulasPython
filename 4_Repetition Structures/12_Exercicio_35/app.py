saque = int(input("Quanto deseja sacar em dinheiro? "))

nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0

while saque > 0:

  while saque >= 100:
    nota100 = nota100 + 1
    saque = saque - 100
  while saque >= 50:
    nota50 = nota50 + 1
    saque = saque - 50
  while saque >= 20:
    nota20 = nota20 + 1
    saque = saque - 20
  while saque >= 10:
    nota10 = nota10 + 1
    saque = saque - 10
  while saque >= 1:
    nota1 = nota1 + 1
    saque = saque - 1

print("Você esta sacando %d notas de 100, %d notas de 50, %d notas de 20, %d notas de 10 e %d notas de 1." % (nota100, nota50, nota20, nota10, nota1))



