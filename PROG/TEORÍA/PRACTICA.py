t=(10,20,30,40,50,60,70,80)

i=0
suma=0
while i <= 7:
    suma = suma + t[i]
    i += 1

print(suma)
suma=0

for numero in t:
    print(numero)
    suma=suma+numero

print(suma)