palabra= str(input("Dime una palabra: "))

palabra_invertida= palabra[::-1]

print(palabra)
print(palabra_invertida)

if palabra == palabra_invertida:
    print("La palabra es palíndrome")
else:
    print("La palabra no es palíndrome")

