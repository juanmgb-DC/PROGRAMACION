positivos= 0
negativos= 0
ceros= 0


numeros= [1,0,-3,3,6,0,-2,-7,-9,8]

for num in numeros:
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    elif num == 0:
        ceros += 1



print(f"Cantidad de numeros positivos: {positivos}")
print(f"Cantidad de numeros negativos: {negativos}")
print(f"Cantidad de numeros ceros: {ceros}")


