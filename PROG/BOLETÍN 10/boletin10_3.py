class Data:
    def __init__(self,dia,mes,ano):
        self.dia = int(dia)
        self.mes = int(mes)
        self.ano = int(ano)

    def setAno(self,ano):
        if ano > 1970 and ano < 2999:
            self.ano = ano
        else:
            return "Ano invalido (1970-2999)"

    def getAno(self):
        return self.ano

    def setMes(self,mes):
        if 0 < mes < 13:
            self.mes = mes
        else:
            return "Mes invalido (1-12)"

    def setDia(self,dia):
        if dia < 1 or dia > 31:
            return "Error, día no valido"
        elif self.mes == 1 or self.mes == 3 or self.mes == 5 or self.mes == 7 or self.mes == 8 or self.mes == 10 or self.mes == 12 and 0 < dia < 32:
            self.dia = dia
        elif self.mes == 2 and 0 < dia < 30:
            self.dia = dia
        elif self.mes == 4 and 0 < dia < 31:
            self.dia = dia
        elif self.mes == 6 and 0 < dia < 31:
            self.dia = dia
        elif self.mes == 9 and 0 < dia < 31:
            self.dia = dia
        elif self.mes == 11 and 0 < dia < 31:
            self.dia = dia
        else:
            return "ERROR"


    def getDia (self):
        return self.dia

    def formatoData (self):
        return f"{self.dia} / {self.mes} / {self.ano}"


data = Data(23,11,2007)
print(data.formatoData())
print(data.setMes(2))
print(data.setDia(29))
print(data.formatoData())

