dicionario = {
    "testando":2,
    "nome":"iago",
    "idade":21
}
print(dicionario)

print("nome" in dicionario)
print("idade" in dicionario)
print("corinthians" in dicionario)
print("sobrenome" in dicionario)

if "nome" in dicionario:
  print("O seu nome é %s" % dicionario["nome"])

if "sobrenome" in dicionario:
  print("O seu sobrenome é %s" % dicionario["sobrenome"])