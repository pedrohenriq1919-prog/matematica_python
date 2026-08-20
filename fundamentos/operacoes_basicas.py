x = int(input("Insira o valor de x: "))
y = int(input("Insira o valor de y: "))
z = int(input("Insira o valor de z: "))

print(f"Valores inseridos: x = {x}, y = {y}, z = {z}")

soma = x + y + z
subtracao = x - y - z
divisao = x / y / z
multiplicacao = x * y * z
divisao_inteira = x // y // z

resultado = soma + subtracao + divisao + multiplicacao + divisao_inteira

if resultado > 100:
    print("O resultado é maior que 100")
else:
    print("O resultado é menor ou igual a 100")

#Utilizando for e while
x = 1000
y = 0

while x >= 1:
    x = x / 2
    y += 1 
    print(y)