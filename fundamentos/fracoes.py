import math
#Operacoes com fracoes
a = 3/4 + 2/5 * (5/6 - 1/3)
print(a)

b = (2/3 + 1/6) * 3/5
print(b)

c = (5/6 - 3/8) * (4/5 + 7/10) 
print(c)

d = 7/9 / (5/6 - (2/3 * 3/4)) + 1/3
print(d)

e = (3/5 + 2/7 * (14/9 - 1/3)) / 4/3
print(e)

f = 5/6 - (2/9) / (7/8) + 1/4 * (3/5 + 5/12)
print(f)

z = 3/4 - (5/6 * (9/10 - 2/5))
print(z)

y = 3/4 + (2/3 - 1/6) * 2**2
print(y)

w = (5/2 - math.sqrt(9))**2 + 3**2/math.sqrt(16) - 7/4
print(w)

#Operacoes com potencias e radicais
x = ((2**3 + math.sqrt(16))/3 - (5/2 - 11/2)) - (2**2 - (math.sqrt(25)/5))
print(x)

#Utilizando o loop for para exibir os resultados de variáveis
x1 = 4/2 + math.sqrt(16) - (math.sqrt(9) + 3**3)
x2 = 10/5 + 2**3 - (math.sqrt(4))**2

for i in range(int(x1), int(x2)):
    print(i)

#Exercício while
x = 2
y = 0

while x <= 32:
    x = x * (3/2)
    y += 1
    print(x)
    print(y)


