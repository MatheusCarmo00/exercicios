a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    a, b = b, a

print("Números primos:")

for numero in range(a, b + 1):

    if numero < 2:
        continue

    primo = True

    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            break

    if primo:
        print(numero)