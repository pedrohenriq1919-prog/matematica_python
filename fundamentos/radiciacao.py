from sympy import symbols, simplify, sqrt, conjugate
import math

#Aplicando a conjugação/simplificação de radicais nas frações
expressao = 1 / (math.sqrt(2) + 1)

resultado = simplify(expressao)

print(f"O resultado da expressão é: {resultado}")

#Demonstrando o conjugado a partir de um número
x = math.sqrt(3) + 2
conjugado_x = conjugate(x)
print(f"O conjugado de x é: {conjugado_x}")

y = math.sqrt(5) - 1
conjugado_y = conjugate(y)
print(f"O conjugado de y é: {conjugado_y}")

#Comparando os conjugados
if conjugado_x == conjugado_y:
    print("Os conjugados são iguais.")
elif conjugado_x > conjugado_y:
    print("O conjugado de x é maior que o conjugado de y.")
elif conjugado_x < conjugado_y:
    print("O conjugado de x é menor que o conjugado de y.") 
else:
    print("Os conjugados são diferentes.") 

#Demonstrando as propriedades de radiciação
a = 3
b = 11

lado_direito = math.sqrt(a * b)
lado_esquerdo = math.sqrt(a) * math.sqrt(b)
resultado = (lado_esquerdo == lado_direito)

a = 4
b = 2

lado_esquerdo = math.sqrt(a / b)
lado_direito = math.sqrt(a) / math.sqrt(b)
resultado = lado_esquerdo == lado_direito
print(resultado)

a = 10
b = 5

a = (7 * math.sqrt(3) - 3) / 2
print(a)

#Exercício 1
x_1 = (
    5/3
    - math.sqrt(108) / math.sqrt(12)
    + (3/5)**-1
)**2 + (
    (2 * math.sqrt(75)) / (5 * math.sqrt(3))
    - math.sqrt(48) / math.sqrt(3)
)

print(x_1)

#Utilizando for e while com radiciação   
for i in range(1, 11):
    x = math.sqrt(i)
    print(i, x)

for i in range(1, 101):
    x = math.sqrt(i)
    if x.is_integer():
        print(i)

#Exercício for
import math

for i in range(1, 11):
    x = i**2 + math.sqrt(i)
    print(x)

