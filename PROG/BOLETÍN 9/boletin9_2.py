class Consumo:
   def __init__(self,km,litros,vMed,pGas):
       self.km=km
       self.litros=litros
       self.vMed=vMed
       self.pGas=pGas


   def getTempo(self):
       tempo = self.km / self.vMed
       return tempo


   def consumoMedio(self):
       return self.litros


   def consumoEuros(self):
       return self.pGas


   def setKms(self,nuevo_km):
       self.km = nuevo_km




   def setLitros(self,nuevos_litros):
       self.litros=nuevos_litros
       return nuevos_litros


   def setvMed(self,nuevo_vMed):
       self.vMed=nuevo_vMed


   def setpGas(self,nuevo_pGas):
       self.pGas=nuevo_pGas


   def amosarTodo(self):
       return (f"Tempo: {self.getTempo()}\n"
               f"Consumo medio: {self.consumoMedio()}\n"
               f"Consumo euros: {self.consumoEuros()}")






mi_consumo= Consumo(1000,50,120,1.57)


print(mi_consumo.amosarTodo())
print(mi_consumo.consumoMedio())
print(mi_consumo.setLitros(60))
print(mi_consumo.amosarTodo())
print(mi_consumo.vMed)
