print("Bom dia! Este é um comunicado do RH, estamos recebendo um aumento no salário devido ao dicídio de 2022 solicitado pelo sindicato.")
print("O aumento é de 13%, para saber qual o novo valor do seu salário, digite aqui quanto você está ganhando(Valor bruto).")

salario_atual = float(input("Digite o seu salário bruto: "))
aumento = salario_atual * 0.13
novo_salario = salario_atual + aumento

print("O aumento para você foi de: R$%.2f, agora o seu novo salário a partir de Fevereiro é de: R$%.2f. Para maiores informações, contate o RH no ramal 3099." % (aumento, novo_salario))
