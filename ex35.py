a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

soma = 0

for numero in range(menor + 1, maior):
    if numero % 2 != 0:
        soma += numero

print("Soma dos números ímpares:", soma)