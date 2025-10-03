
import math
def crearMenu():

   print("De que figura quere calcular o área:")
   print("1. Area Rectangulo")
   print("2. Area Triangulo")
   print("3. Area Circulo")
   print("4. Salir")
   print("Elixa opción:")

def calcularRectangulo(base, altura):
  return base*altura

def calcularTriangulo(base, altura):
  area = calcularRectangulo(base, altura)/2
  return area

def calcularCirculo(radio):
  return math.pow(radio,2)* math.pi

def recollerParametros(opcion):
   if opcion == 1 or opcion == 2:
     base = float (input("Escribe a base:"))
     altura = float(input("Escribe a altura:"))
     return base, altura
   elif opcion == 3:
      radio = float(input("Escribe o radio:"))
   return radio



def exercicioBoletin4_2():

       opcion = 0
       while opcion !=4:
          crearMenu()
          opcion = int(input("Escribe una opcion: "))
          if opcion > 0 and opcion < 5:
             if opcion == 1 or opcion ==2:
                  base, altura = recollerParametros(opcion)
                  if opcion == 1:
                      area = calcularRectangulo(base, altura)
                      print("O área do rectangulo é: ", area)
                  if opcion == 2:
                      area = calcularTriangulo(base, altura)
                      print ("O área do triangulo é: ", area)
             elif opcion == 3:
                      radio = recollerParametros(opcion)
                      area= calcularCirculo (radio)
                      print("O área do circulo é: ", area)

exercicioBoletin4_2()
