colores={"vermello":"red",
         "amarelo":"yellow",
         "azul":"blue"
         }

print(colores["vermello"])
print(colores.keys())
for k in colores.keys():
    print(colores[k])

print ()

print(colores.values())
for color in colores.values():
    print(color)

print (colores.items())

for clave_valor in colores.items():

    print("A clave é: ", clave_valor[0] , "\n0 valor é: ",clave_valor[1])

colorado = colores.pop("vermello")
print(colorado)
print(colores.items())
print("vermello" in colorado)