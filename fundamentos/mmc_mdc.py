import math

#Usando MMC para descobrir quando os arquivos serão executados
arquivo_a = "Executado em 6 segundos 10 arquivos"
arquivo_b = "Executado em 8 segundos - 12 arquivos"
arquivo_c = "Executado em 12 segundos - 24 arquivos"
arquivo_d = "Executado em 15 segundos - 30 arquivos"
mmc = math.lcm(6, 8, 12, 15)
mdc = math.gcd(10, 12, 24, 30)

print(f"Melhor agrupamento dos programas: {mdc} grupos.")
print(f"Os arquivos serão executados juntos a cada {mmc} segundos.")

#Aplicando o Algoritmo de Euclides para descobrir o MDC
def euclides(a, b):
    while b != 0:
        resto = a % b

        print(f"{a} % {b} = {resto}")

        a = b
        b = resto

    return a


mdc = euclides(48, 18)

print("MDC =", mdc)

#Utilizando IF, ELSE E ELIF
a = 10
b = 20
c = 30

mmc = math.lcm(a, b, c)

if mmc > 50:
    print("O MMC é maior que 50")
else:
    print("O MMC é menor ou igual a 50")

#Utilizando IF, ELSE E ELIF

dados_1 = 35
dados_2 = 20
dados_3 = 15

conjunto_de_dados = [dados_1, dados_2, dados_3]

agrupamento = math.gcd(*conjunto_de_dados)

if agrupamento > 50:
    print("O agrupamento é grande.")
elif agrupamento > 20:
    print("O agrupamento é adequado.")
elif agrupamento > 10:
    print("O agrupamento é pequeno.")
else:
    print("O agrupamento é muito pequeno.")
