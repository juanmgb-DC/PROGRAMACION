import math

entrada = input("Introduce los números separados por comas: ")

numeros = [float(num) for num in entrada.split(',')]

media = sum(numeros) / len(numeros)

desviacion = math.sqrt(sum((x - media) ** 2 for x in numeros) / len(numeros))

print(f"Lista de números: {numeros}")
print(f"Media: {media}")
print(f"Desviación típica: {desviacion}")