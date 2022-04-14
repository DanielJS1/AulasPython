def soma(a,b):
  return a + b

def multiplicacao(a,b):
  return a * b

def operacao(a,b,operador):
  resultado = operador(a,b)
  return resultado


n1 = int(input("Digite um numero: "))

n3 = input("Escolha '+' para soma ou '*' para multiplicacao: ")

n2 = int(input("Digite outro número: "))

if n3 == "+":
  a = operacao(n1, n2, soma)
elif n3 == "*":
  a = operacao(n1,n2,multiplicacao)
else:
  print("Não existe esta opção, otário...")

print(a)
