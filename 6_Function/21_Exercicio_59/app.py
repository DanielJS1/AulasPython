import random

numero_sorteado = random.randint(1,10)

num_escolhido = int(input("Advinhe um número de 1 a 10: "))


if num_escolhido == numero_sorteado:
    print("Caraca! Você acertou, Maluco!")
else: 
    print("O número era %d Puxa! Não foi dessa vez que você conseguiu. Mas não desista! Tente somente durante o programa tá? Vlw!!" % numero_sorteado)


    
    