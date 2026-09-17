import math

n = int(input("Digite N: "))

soma = 0

for i in range(0, n + 1):
    soma += 1 / math.factorial(i)

print("Resultado:", soma)