cont=0
while True:
    cont=cont+1
    if cont%3 !=0:
        continue
    print(cont)
    if cont>20:
        break



# Exemplo de bucle for

t= (100,200,300,400,500)
iteracion= 1

for numero in t:
    iteracion = iteracion + 1
    print("Iteracion",iteracion)
    print("Elemento da tupla",numero)
