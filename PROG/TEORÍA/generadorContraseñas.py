#Genera contraseñas de 6-12 caracteres, simbolos, letras mayusculas y minusculas y numeros

import random
import string


longitud= random.randint(6,12)

caracteres= string.ascii_letters + string.digits + string.punctuation

contraseña= ''.join(random.choice(caracteres) for _ in range (longitud))

print("Contraseña generada:", contraseña)


#Otra opcion

def xeneradorContrasinais(n):
    l = ['123456789', 'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ','$%&/()¨Ç*[]{}']

    i=0
    contrasinal=''
    while i<n:
        tipo = random.randint(0,3)
        iSim = random.randint(0,len(l[tipo])-1)
        contrasinal = contrasinal + l[tipo][iSim]
        i+=1
    return contrasinal
while True:
    n = int(input("Introduce a lonxitude do contrasinal (0 para sair): "))
    if n >= 6 and n <=12:
        print(xeneradorContrasinais(n))
    elif n == 0:
        break
    else:
        print("A lonxitude é entre 6 e 12")






