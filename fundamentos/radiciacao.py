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



