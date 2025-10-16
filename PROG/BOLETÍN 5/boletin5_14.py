suma= 0
contador= 0

while contador < 10:
    numero= (int(input("Introduce un número (999 para saír): ")))

    if numero == 999:
        print("Operación finalizada")
        break
    suma += numero
    contador +=1

print(f"A suma total é: {suma}")