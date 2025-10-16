fallos= 0
acerto = False
palabra= "frigorifico"
palabraGuions=''
for letra in palabra:
    palabraGuions = palabraGuions + '_'

while acerto == False or fallos <= 7:
    print("A palabra a acertar é: "+ palabraGuions)
    palabraLetra = input("Introduce la palabra o la letra: ")
    if len(palabraLetra) != 0:
        if palabraLetra != 1:
            if palabraLetra == palabra:
                acerto=True
                print("Felicidades, acertaches")
            else:
                fallos= fallos + 1
        else:
            encontrado = False
            for i, caracter in enumerate(palabra):
                if palabraLetra == caracter:
                    palabraGuions = palabraGuions[:i] + caracter + palabraGuions
                    encontrado = True
            if encontrado == True:
                if palabraGuions == palabra:
                    print("Noraboa, acertaches a palabra" + palabra)
                    acerto=True
            else:
                fallos = fallos + 1