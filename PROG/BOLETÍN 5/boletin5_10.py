while True:
    try:
       b= int(input("Cal é a base do rectangulo: "))
       a= int(input("Cal é o área do rectangulo: "))
    except ValueError:
         print("Error, letras no permitidas")
    if a > 0 and b > 0:
        area= b*a
        print("O área do rectangulo é", area)
        break
    else:
        print("Non pode tener datos negativos")
