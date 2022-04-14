def comprimento(texto):
  
  resposta = ""

  if len(texto) > 20:
    print("Este texto é muito longo!")
  elif len(texto) <= 20:
    print("Este texto é muito curto")
  else:
    print("Texto inválido.")

  return resposta

textoUsuario = input("Digite uma frase: ")

comprimento(textoUsuario)
