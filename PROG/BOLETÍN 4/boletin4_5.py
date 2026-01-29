def calcular_letra_dni(dni):
    letras= [ "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
        "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    return letras [dni % 23]

while True:
    try:
        dni=int(input("Escribe o numero do DNI: "))
    except ValueError:
        print("Debes introducir solo numeros")
        continue

    if 10000000 <= dni <= 99999999:
        letra= calcular_letra_dni(dni)
        print(f"El DNI completo es: {dni}{letra}")
        break
    else:
        print("Introduce 8 dígitos")




