"""
Escribir unha función que indique si duas fichas de dominó encaixan.
As fichas son recibidas en duas tuplas, por exemplo: (3,4) e (5,4).
A función devolta un booleano co resultado do encaixe.

"""


def encaixan(ficha1,ficha2):
    return ficha1[0] in ficha2 or ficha2[1] in ficha2

print(encaixan((3,5),(4,6)))











