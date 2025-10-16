lista1= [1,2,3]
lista2= [-1,0,2]

producto_escalar = 0


for i in range(len(lista1)):
    producto_escalar += lista1[i] * lista2[i]

print("El producto escalar de los vectores es: ",producto_escalar)