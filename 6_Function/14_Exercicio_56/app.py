def todos_dados(nome, idade, profissao, f):
  apresentacao = f(nome, idade, profissao)
  return apresentacao

def apresenta_os_dados(nome, idade, profissao):
  mensagem = "O cliente se chama %s, com idade %d anos e é um %s" % (nome, idade, profissao)
  return mensagem

nome = input("Digite seu Nome: ")
idade = int(input("Digite sua idade: "))
profissao = input("Qual a sua Profissao: ")

mensagem = apresenta_os_dados(nome,idade,profissao)
print(mensagem)
