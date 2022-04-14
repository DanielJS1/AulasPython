class Carro:
    def __init__(self, portas, motor, teto_solar, fabricante, preco):
        self.portas = portas
        self.motor = motor
        self.teto_solar = teto_solar
        self.fabricante = fabricante
        self.preco = preco

Porshe_911 = Carro(2,"V8","Sim","Porshe",498.000)

Camaro = Carro(2,"V8","Não","Chevrolet",198.00)

print(Porshe_911.portas)

if Porshe_911.teto_solar == "Não":
    print("A porshe não tem teto solar.")
else:
    print("A porshe tem teto solar.")

if Camaro.motor == "V8":
    print("O camaro tem o motor V8.")
else:
    print("Este camaro não tem motor V8.")

print("Just test")

print("Secund test in GitHub.")