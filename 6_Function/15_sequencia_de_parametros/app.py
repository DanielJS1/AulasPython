def soma_todos(*nums):
  soma = 0
  for num in nums:
    soma += num
  
  return soma

s = soma_todos(5,5,4,342,43,24)

print(s)