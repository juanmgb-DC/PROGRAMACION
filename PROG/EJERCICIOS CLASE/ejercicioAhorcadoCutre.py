fallos= 0
palabra_secreta= "secreto"
max_intentos= 7
intentos_realizados= 0

while intentos_realizados < max_intentos:
    palabra_usuario= input("Dime una palabra: ").lower()
    if palabra_usuario == palabra_secreta:
        print("Correcto!")
        break
    else:
        intentos_realizados += 1
        fallos += 1
        print(f"Incorrecto, te quedan {max_intentos - intentos_realizados} intentos")
        print("Pista: La palabra tiene",len(palabra_secreta),"digitos")
print("Fallos: ",fallos)

