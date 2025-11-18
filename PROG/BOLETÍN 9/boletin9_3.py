class Coche:
   def __init__(self):
       self.velocidade = 0
   def getVelocidade(self):
       return f"Velocidad: {self.velocidade}"
   def getAcelerar(self,valor):
       self.velocidade += valor
       return f"Velocidad aumentada: {self.velocidade}"
   def getFrenar(self,menos):
       self.velocidade -= menos
       if self.velocidade < 0:
           self.velocidade = 0
       return f"Velocidad reducida: {self.velocidade}"




mi_coche=Coche()
print(mi_coche.getVelocidade())
print(mi_coche.getAcelerar(100))
print(mi_coche.getFrenar(50))
