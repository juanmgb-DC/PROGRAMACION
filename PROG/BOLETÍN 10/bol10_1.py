class Persoa:
    def __init__(self, nome, direccion, dni):
        self.nome= str(nome)
        self.direccion= str(direccion)
        self.dni= str(dni)

    def setNome(self,nome):
        if nome(type) == str:
            self.nome = nome
        else:
           return ("Nome non valido")

    def getNome(self):
        return self.nome

    def setDireccion(self,direccion):
        if direccion(type) == str:
            self.direccion = direccion
        else:
           return ("Direccion non valida")

    def getDireccion(self):
        return self.direccion



    def setDni(self,dni):
        if dni(type) == str:
            self.dni = dni
        else:
            return("Dni non valido")

    def getDni(self):
        return self.dni

class DniNonValido(Exception):
 pass



Juan = Persoa("Juan","Pi y Margall","54230432C")

print (Juan.getDireccion())
print (Juan.getNome())
print (Juan.getDni())

try:
   print(Juan.setDni(12131))
except TypeError:
  raise DniNonValido ("El Dni no es valido")