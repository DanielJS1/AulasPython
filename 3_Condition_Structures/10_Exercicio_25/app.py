n1 = int(input("Digite um número: "))

if n1 > 10:
    if n1 < 20:
        n1x2 = n1 * 2
        print("Este número multiplado por 2 é: %d" % n1x2)
    else:
        n1x5 = n1 * 5
        print("Este número multiplicado por 5 é: %d" % n1x5)
else:
    print("Para prosseguir, digite um número maior que 10.")