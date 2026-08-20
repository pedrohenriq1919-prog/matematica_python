import math 

#Demonstrando todas as propriedades da potência
#Produto de potências com mesma base
a = 2
m = 3
n = 4

lado_esquerdo = a**m * a**n
lado_direito = a**(m + n)

print(lado_esquerdo)
print(lado_direito)
print(lado_esquerdo == lado_direito)

#Divisão de potências com mesma base
a = 5
x = 8
y = 3

lado_esquerdo = a**x / a**y
lado_direito = a**(x - y)

print(lado_esquerdo)
print(lado_direito)
print(lado_esquerdo == lado_direito)

#Potência de uma potência
a = 20
m = 3

lado_esquerdo = (a**m)**2
lado_direito = a**(m * 2)

print(lado_esquerdo)
print(lado_direito)
print(lado_esquerdo == lado_direito)

#Potência de um produto
a = 3
b = 4
n = 2

lado_esquerdo = (a * b)**n
lado_direito = a**n * b**n

print(lado_esquerdo)
print(lado_direito)
print(lado_esquerdo == lado_direito)

#Potência de uma divisão
a = 2
b = 4
n = 5

lado_esquerdo = (a / b)**n
lado_direito = (a**n) / (b**n)

print(lado_esquerdo)
print(lado_direito)
print(lado_esquerdo == lado_direito)

#Expoente 0 
a = 0
resultado = a**0 
print(resultado)
print(resultado == 1)

#Expoente negativo
a = 2
n = 4

resultado = 1/a**n
print(resultado)

#Programa utilizando if/else
a = 2
m = 4
n = 8

lado_esquerdo = a**m * a**n
lado_direito = a**(m + n)

if lado_esquerdo == lado_direito:
    print(f"A propriedade está correta!")
else:
    print(f"A propriedade está incorreta!")

#Programa interativo com o usuário
a = int(input("Digite o valor da base:"))
m = int(input("Digite o valor do primeiro expoente:"))
n = int(input("Digite o valor do segundo expoente:"))

print(f"O valor da base é: {a}")
print(f"O valor do primeiro expoente é: {n}")
print(f"O valor do segundo expoente é: {m}")

lado_esquerdo = a**m * a**n
lado_direito = a**(m + n)

#Utilizando for e while com potências
for i in range(1, 11):
    print(2**i)

for i in range (2, 11, 2):
    print(i**3)

soma_potencia = 0

for i in range(2, 4):
    soma_potencia += i**2
print(soma_potencia)

#Calculando quadrados e cubos usando for
for i in range(2, 7):
    resultado = i**2
    print(resultado)

for i in range (3, 10):
    x = i**3
    print(x)





