maior = 0
menor = None

for i in range(100):
    numero = float(input("Digite um número positivo: "))

    if numero > 0:
        if numero > maior:
            maior = numero

        if menor is None or numero < menor:
            menor = numero
    else:
        print("Digite somente valores positivos.")
        i -= 1

print("Maior valor:", maior)
print("Menor valor:", menor)