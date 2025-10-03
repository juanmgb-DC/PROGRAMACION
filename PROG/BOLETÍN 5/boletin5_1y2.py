#1 : Escribir un ciclo definido para imprimir por
# pantalla tódolos números entre	10 e 20.

t=[10,11,12,13,14,15,16,17,18,19,20]

for numero in t:
    print(numero)

#2 Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius.
# Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.

temperatura= input("Escribe o valor en celsius:")
temperatura= float(temperatura)

F = 9/5 * temperatura + 32


print(f"{temperatura} grados celsius son {F} grados Fahrenheit")


