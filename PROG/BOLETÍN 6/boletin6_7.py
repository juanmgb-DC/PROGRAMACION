palabra= input("Escribe una palabra: ")
vocales= "aeiou"


for vocal in vocales:
    cantidad= palabra.count(vocal)
    print(vocal,cantidad)
