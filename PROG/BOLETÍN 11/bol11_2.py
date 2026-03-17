nombre_fichero = input("Nombre del fichero:  ").lower()
archivo = f"{nombre_fichero}.txt"

while True:

    print("1. Engadir nota")
    print("2. Ver numero de cada palabra")
    print("3. Saír")
    opcion = input("Opción: ")

    if opcion == "1":
         nota = input("Nota: ")
         f = open(archivo, "a")
         f.write(nota + "\n")
         f.close()

    if opcion == "2":
        try:
                cuenta = {}
                f = open(archivo,"r")
                for linea in f:
                   palabras = linea.split()
                   for palabra in palabras:
                       palabra = palabra.lower()
                       if palabra in cuenta:
                           cuenta[palabra] += 1
                       else:
                           cuenta[palabra] = 1
                for palabra, veces in cuenta.items():
                    print(palabra,":",veces)
                f.close()

        except:
                print("No hay lineas")

    if opcion == "3":
        break