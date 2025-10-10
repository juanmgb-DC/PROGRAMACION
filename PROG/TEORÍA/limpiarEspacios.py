#Escribe un texto y quitale los espacios

#Con strip
texto1= "     Texto     "
print(texto1)
texto2= texto1.strip()
print(texto2)

#Sin trip
def limpiadorCadeas(cadea):
    for c in cadea:
        if c==' ':
             cadea = cadea[1:]
        else:
            break
    for i in range(len(cadea)-1, -1, -1):
        if cadea[i] == ' ':
            cadea = cadea[:i]
        else:
            break
    return cadea

limpa = limpiadorCadeas('    Pepiño grilo     ')
print('      Pepiño grilo      ')
print(limpa,'|')



