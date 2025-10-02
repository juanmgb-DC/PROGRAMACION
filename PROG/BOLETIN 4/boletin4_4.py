uno_veinte={
    0: "",
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve",
    10: "diez",
    11: "once",
    12: "doce",
    13: "trece",
    14: "catorce",
    15: "quince",
    16: "dieciseis",
    17: "diecisiete",
    18: "dieciocho",
    19: "diecinueve",
    20: "veinte"
     }
decenas={ 2: "veinti",
    3: "treinta",
    4: "cuarenta",
    5: "cincuenta",
    6: "sesenta",
    7: "setenta",
    8: "ochenta",
    9: "noventa"
          }



while True:
    n= int(input("Escribe un numero: "))

    sn=str(n) # "34"
    sn1=sn[0] # "3"
    sn2=sn[1] # "4"
    ene1=int(sn1) # 3
    ene2=int(sn2)   # 4

    if 1 <= n <= 99:
        if n <= 20:
            print("El numero seleccionado es",uno_veinte[n])
        elif n <= 29:

            print("El numero selecciconado es",decenas[ene1] + uno_veinte[ene2])
        elif n > 29:
            print("El numero seleccionado es",decenas[ene1],"y",uno_veinte[ene2])
        break
    else:
        print("Numero no valido")

