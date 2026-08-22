#Demonstrando os produtos notáveis mais comuns
x = (2 + 3)**2
y = x**2 + 2*2*3 + 3**2
print(f"Quadrado da soma: {y}")

a = (3 - 4)**2
b = 3**2 + 2*3*4 + 4**2
print(f"Quadrado da diferença: {b}")

m = (9 - 8)(9 - 8)**2
n = 9**2 - 8**2
print(f"Quadrado da diferença: {n}")

#Programa validador de produtos notáveis
while True:

    n = int(input("Digite o valor de n: "))

    for i in range(1, n + 1):

        formula = i**2 + 2*i*3 + 3**2

        multiplicacao = (i + 3) * (i + 3)

        if formula == multiplicacao:
            print(f"\nx = {i}")
            print(f"Fórmula: {formula}")
            print(f"Multiplicação: {multiplicacao}")
            print("Os resultados são iguais.")
        else:
            print("Os resultados são diferentes.")

    continuar = input("\nDeseja executar novamente? (s/n): ")

    if continuar == "n":
        break



 

