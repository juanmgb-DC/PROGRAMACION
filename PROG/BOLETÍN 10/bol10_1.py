class Persoa:
    def __init__(self, nome, direccion, dni):
        self.nome= (nome)
        self.direccion= (direccion)
        self.dni= (dni)

    def setNome(self,nome):
        if isinstance(nome,str):
            self.nome = nome
        else:
           return ValueError("Nome non valido")

    def getNome(self):
        return self.nome

    def setDireccion(self,direccion):
        if isinstance(direccion,str):
            self.direccion = direccion
        else:
           return ValueError("Direccion non valida")

    def getDireccion(self):
        return self.direccion



    def setDni(self,dni):
        if isinstance(dni,str):
            self.dni = dni
        else:
            return DniNonValido("Dni non valido")

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
except DniNonValido as e:
    print(e)