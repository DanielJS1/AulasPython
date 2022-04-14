idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Você pode entrar na balada.")

    metodo_pagamento = int(input("Como você vai pagar a entrada(1 - Dinheiro/PIX | 2 - Cartão): "))

    if metodo_pagamento == 1:
        print("A fila de dinheiro é a fila 1.")
    if metodo_pagamento == 2:
        print("A fila para cartão é a 2.")
else:
    print("Você não pode entrar na balada.")
