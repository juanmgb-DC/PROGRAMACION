
asignaturas=["Matematicas","Fisica","Quimica","Historia","Lingua"]
notas=[]
asignaturas_suspensas=[]
for asignatura in asignaturas:
    nota= int(input("Que nota sacaste en " + asignatura))
    if nota < 5:
        notas.append(nota)
        asignaturas_suspensas.append(asignatura)
i = 0
for asignaturasuspensa in asignaturas_suspensas:
    print("Debes de recuperar", asignaturas_suspensas[i])
    i += 1







