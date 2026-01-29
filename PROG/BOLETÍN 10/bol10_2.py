class Deportista:
    def __init__(self,club,deporte,licencia):
        self.club = str(club)
        self.deporte = str(deporte)
        self.licencia = str(licencia)

    def setClub(self,club):
        if club(type) == str:
            self.club = club
        else:
            return ("Error, Club no valido")

    def getClub(self):
        return self.club

    def setDeporte(self,deporte):
        if deporte(type) == str:
            self.deporte = deporte
        else:
            return ("Error, Deporte non valido")

    def setLicencia(self,licencia):
        if len(licencia) == 13:
            if licencia[:4].isdigit():
                if licencia[4:7].isalpha():
                    if licencia[8:13].isdigit():
                        self.licencia = licencia
                        return "Licencia actualizada"
                    else:
                        return "Error ultimos numeros"
                else:
                    return "Error letras"
            else:
                return "Error primeros numeros"
        else:
            return "Error longitud"

    def getLicencia(self):
        return self.licencia


deportista = Deportista("Elche","Futbol","2026fut542304")

print(deportista.setLicencia("2026fut542323"))
print(deportista.getLicencia())