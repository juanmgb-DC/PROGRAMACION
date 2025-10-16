while True:
    numero_str= int(input("Introduce un numero (Introduce 0 para sair): "))
    numero= int(numero_str)

    if numero == 0:
        break


    print("Tabla de multiplicar:")
    for i in range(1,11):
        resultado= numero * i
        print(f"{numero} * {i} = {resultado}")