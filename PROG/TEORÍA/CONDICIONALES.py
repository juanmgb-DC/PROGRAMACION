temp=0

if temp <= 0:
    print("Vai un frio do carallo")
elif temp > 0 and temp <= 10:
    print ("Vai moito fresco")
elif temp > 10 and temp <= 20:
    print ("Vai fresco")
elif temp >20 and temp<=30:
    print ("Isto templase")
else:
    print("Vair un calor do carallo")



if temp >15:
    valoracionAtmosferica="Calor"
else:
    valoracionAtmosferica="Frio"

valoracionAtmosferica= "Calor" if temp>15 else "Frio"