graos = 1
total = 0

for casa in range(1, 65):
    print("Casa", casa, ":", graos, "grãos")

    total += graos
    graos *= 2

print("Total de grãos:", total)