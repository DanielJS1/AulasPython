nome = "Daniel José"
saldo = 23.98
print("Olá, %s. Seja bem-vindo ao BB." % nome)
deposito = (float(input("Deposite um valor na sua conta: ")))

saldo = saldo + deposito
debito_automatico = 125.98

saldo = saldo - debito_automatico

print("Foi debitada a fatura do seu cartão com a função débito automático, para desabilitar acesse as configurações de conta.")
print("Seu novo saldo é de: %.2f." % saldo)
