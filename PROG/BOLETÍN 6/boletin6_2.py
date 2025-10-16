numeros = []

print("Introduce os 6 números gañadores da lotaría primitiva:")


while len(numeros) < 6:
    try:
        num = int(input(f"Número {len(numeros) + 1}: "))
        if num < 1 or num > 49:
            print("O número debe estar entre 1 e 49.")
        elif num in numeros:
            print("Este número xa foi introducido.")
        else:
            numeros.append(num)
    except ValueError:
        print("Por favor, introduce un número válido.")


numeros.sort()

print("\nNúmeros gañadores ordenados de menor a maior:")
print(numeros)