

print("1")


cadena_de_texto= "Isto é Python!"

print(len(cadena_de_texto))

print("2")

texto2= "Python"

for t in texto2:
    print(t)

print("3")

texto3= "Python para todos"
print(texto3[::-1])

print("4")

texto4= "Guido Van Rossum creou Python"
texto4_sin_espacios= texto4.replace(" ","")
print(texto4_sin_espacios)

print("5")

texto5= "Python Python Python"
vocales="aeiou"
consonantes= "bcdfghjklmnñpqrstvwxyz"


for vocal in vocales:
    cantidad= texto5.lower().count(vocal)
    print(vocal,cantidad)
for consonante in consonantes:
    cantidadc= texto5.lower().count(consonante)
    print(consonante,cantidadc)

print("6")

texto6= "www.phytonparatodos.com"
textoprimero= texto6[:10]
textosegundo= texto6[10:]

print("La primera parte: ", textoprimero)
print("La segunda parte: ", textosegundo)
print("Texto completo: ", textoprimero+textosegundo)

print("7")
texto7= "Phytoneros"
texto7mayus= texto7.upper()
texto7minus= texto7.lower()
print("En mayusculas: ",texto7mayus)
print("En minusculas: ", texto7minus)

print("8")

string1="Python"
string2="JavaScript"
if string1 != string2:
    print(string1,"y",string2,"no son iguales")

print("9")

texto9="Jeve jeve jeve"
texto9solucion= texto9.replace("e","a")
print(texto9solucion)


print("10")

texto10= "Ola, son alumno de DAM1, e son programador desde o 2025"
numeros="0,1,2,3,4,5,6,7,8,9"
letras="abcdefghijklmnopqrstuvwxyz"
espacios=" "
texto10_minus= texto10.lower()
total_numeros=0
total_letras=0
total_espacios=0

for numero in texto10_minus:
    if numero in numeros:
        total_numeros += 1
print("Total de numeros: ", total_numeros)

for letra in texto10_minus:
    if letra in letras:
        total_letras += 1
print("Total de letras: ", total_letras)

for espacio in texto10_minus:
    if espacio in espacios:
        total_espacios += 1
print("Total de espacios: ", total_espacios)


