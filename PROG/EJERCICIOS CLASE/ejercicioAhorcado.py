fallos= 0
acerto = False
palabra= "frigorifico"
palabraGuions=''
for letra in palabra:
    palabraGuions = palabraGuions + '_'

while acerto == False and fallos <= 7:
    print("A palabra a acertar é: "+ palabraGuions)
    print("Ten", str(7-fallos),"oportunidades")
    palabraLetra = input("Introduce la palabra o la letra: ")
    if len(palabraLetra) != 1:
        if len(palabraLetra) != 1:
            if palabraLetra == palabra:
                acerto=True
                print("Felicidades, acertaches")
                break
            else:
                print(palabraLetra,"non é correcta")
                fallos= fallos + 1
                if fallos == 7:
                    break
    else:
        encontrado = False
        for i, caracter in enumerate(palabra):
             if palabraLetra == caracter:
                palabraGuions = palabraGuions[:i] + caracter + palabraGuions[i+1:]
                encontrado = True
        if encontrado == True:
             if palabraGuions == palabra:
                print("Noraboa, acertaches a palabra" + palabra)
                acerto=True
        else:
            fallos = fallos + 1
def eliminar_acentos(palabra):
    for i, letra in  enumerate(palabra):
        if "á" in letra:
            palabra = palabra.replace('á','a')
            palabra= palabra[:i] + 'a' + palabra[i+1:]




