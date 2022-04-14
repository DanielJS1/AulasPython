def multiplica_todos(*nums):
  multi = 1
  for num in nums:
    multi *= num
  
  return multi

s = multiplica_todos(2,2,2)

print(s)