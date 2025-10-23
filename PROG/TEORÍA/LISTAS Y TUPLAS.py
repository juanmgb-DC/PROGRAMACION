l =[10, 20, [30,"Trinta", "XXX"],40, 50]
t =(10,20,30,40,50,60,70,80,90,100)
print (l[2][1])
print(l[-3])
print(t[0])
print(t[1:3])
print(t[1:9:2])


print("")
print(t[::-1])
print(l)
print(t[1:10:2])
#Diccionario
print("")
colores = {"verde":"green",
           "vermello": "red",
           "azul": "blue"}
print(colores["verde"])
print(colores["vermello"])

print(colores.keys())
print(colores.values())

for color in colores.values():
    print(color)
print("")

for clave in colores.keys():
    print(colores[clave])


l2=list(['a','b','c'])
t2=tuple([1,2,3,4,5])

print(len(t2))
l2.append('d')
print(l2)
l2.extend(['e','f','g'])
print(l2)
l2.insert(7,'h')
print(l2)
l2.append('d')
l2.remove('d')
print(l2)
print(l2.pop(4))
print(l2)

l2.count("e")
print(l2)
