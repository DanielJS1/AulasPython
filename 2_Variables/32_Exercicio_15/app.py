valor1 = float(input("Ganhe 10 reais! Digite quanto tem na conta(Incluindo centavos): "))
valor2 = int(input("Quanto você irá ganhar mesmo?? "))

novo_valor = valor1 + float(valor2)

print("Parabéns!!! Você acertou, acaba de ganhar 10 reais. Saldo na sua conta agora é de: %.2f" % novo_valor)