class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

daniel = Pessoa("Daniel", 22, "Técnico")

print(type(daniel))

print(daniel.nome)
print(daniel.idade)
print(daniel.profissao)

if daniel.nome == "Daniel":
    print("O nome é Daniel.")

nome = daniel.nome

print(nome)