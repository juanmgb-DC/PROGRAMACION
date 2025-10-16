



n = int(input("Introduce un número: "))

for i in range(1, n + 1):
    espazos = ' ' * (n - i)
    estrelas = '* ' * i
    print(espazos + estrelas)