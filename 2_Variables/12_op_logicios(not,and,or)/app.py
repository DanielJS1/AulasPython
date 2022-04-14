#not = usado para inverter o booleano;
#and = usado como "e"(fulano "e" ciclano);
#or  = usado como "ou"(fulano "ou" ciclano),

#começando com NOT

verdadeiro = True
falso = False

print(not verdadeiro)
print(not falso)

print(not(5 > 2))
print(not(5 < 2))

#Indo para o AND

a = 5
b = 10
c = 2
d = 8

print(a > b and c > d)
print(a > b and c < d)
print(c < d and b < d)

print(a < b and b > c)

#Indo para o OR

a = 5
b = 10

print(a > b or b == 11)

print(b > a or b == 10)
print(a > b or b == 10)
print(b > a or b == 20)

nome = "Daniel"
idade = 21

print(nome == "Deyverson" or idade > 18)
