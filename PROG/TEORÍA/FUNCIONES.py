

def calcularAreaTriangulo(base, altura):
    area=base * altura /2
    return area

print (calcularAreaTriangulo(4,3))

def suma(n1, n2, *outrosNumeros):
    suma= n1 + n2
    for n in outrosNumeros:
        suma = suma + n
    return suma

print(suma(3,2,1, 2, 3))

def datosPersoa (dni, nome, **datosExtendidos):
    print("O dni é :", dni)
    print("O nome é :", nome)
    for k, v in datosExtendidos.items():
        print(k,"é", v)
    #definir como traballo cos datos



datosPersoa(333J, "Manuel", altura=1.82, peso= 71)


lista = [1,2,3,4,5]
def duplicaLista(l):
    for i, num in enumerate(l):
        l[i]= num *2
    return l
print (duplicaLista(lista))
print(lista)