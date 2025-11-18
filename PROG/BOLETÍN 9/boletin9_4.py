class Conta:
   def __init__(self,nome,numero,interese,saldo):
       self.nome = nome
       self.numero = numero
       self.interese = interese
       self.saldo = saldo


   def getNome(self):
       return f"Nome: {self.nome}"
   def getNumero(self):
       return f"Numero: {self.numero}"
   def getInterese(self):
       return f"Interese: {self.interese}"
   def getSaldo(self):
       return f"Saldo: {self.saldo}"


   def setNome(self,nuevo_nome):
       self.nome=nuevo_nome
       return f"Nuevo nome: {nuevo_nome}"
   def setNumero(self,nuevo_numero):
       self.numero=nuevo_numero
       return f"Nuevo numero: {nuevo_numero}"
   def setInterese(self,nuevo_interese):
       self.interese=nuevo_interese
       return f"Nuevo interese: {nuevo_interese}"
   def setSaldo(self,nuevo_saldo):
       self.saldo=nuevo_saldo
       return f"Nuevo saldo: {nuevo_saldo}"




   def depositar (self,valor):
       self.saldo += valor
       return f"Saldo aumentado: {self.saldo}"


   def retirar (self,valor):
       self.saldo -= valor
       if self.saldo < 0:
           self.saldo = 0
       return f"Saldo disminuido: {self.saldo}"


   def transferir (self,destino,valor):
       self.retirar(valor)
       destino.depositar(valor)






cuentaDestino = Conta("Juan",5274,"15%",2500)
cuentaOrigen = Conta("Lucas",1234,"15%",5000)


cuentaOrigen.transferir(cuentaDestino,2000)
print (cuentaOrigen.getSaldo())
print (cuentaDestino.getSaldo())
