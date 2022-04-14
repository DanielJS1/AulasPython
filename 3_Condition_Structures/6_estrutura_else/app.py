poupanca = 500

saque = int(input("Quanto deseja sacar? "))

if saque <= poupanca:
  print("Você sacou R$%d" % saque)
  poupanca = poupanca - saque
  print("Sua poupança tem no momento tem R$%d" % poupanca)
else:
  print("Você não tem saldo para sacar R$%d" % saque)
  print("Sua poupança tem no momento tem R$%d" % poupanca)