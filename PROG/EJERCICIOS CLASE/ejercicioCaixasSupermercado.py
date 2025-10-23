#Supermercado
#Caixas - Cartos en efectivo
#Efectivo =[[(50,13),(20,5),(0'5,12),(0,23,13)]
#App que me de o importe por caixa e o total



efectivo = [['2',[100,1],[50,13],[20,5]],['1',[100,1],[50,13],[20,5]],['3',[50,21],[20,11],[10,7],[0.02,9]]]

def mostrarContidoUnhaCaixa (caixa, totalEfectivoCaixas):
   for contidoCaixa in totalEfectivoCaixas:
       if contidoCaixa[0] == caixa:
           print('O contido da',caixa, "é: ")
           for i in range (1,len(contidoCaixa)):
               if contidoCaixa[i][0] > 2.0:
                   print(contidoCaixa[i][1], "billetes de ",contidoCaixa[i][0], " Euros")
               else:
                   print(contidoCaixa[i][1], "moedas de",contidoCaixa[i][0], "Euros")

mostrarContidoUnhaCaixa('1',efectivo)


caixa1=[[100,1],[50,13],[20,5]]
caixa2=[[50,2],[20,9],[0.20,3],[0.05,23]]
caixa3=[[50,21],[20,11],[10,7],[0.02,9]]

def importe_por_caixa(caixa):
    total=0
    for valor,cantidad in caixa:
        total += valor * cantidad
    return total

print("Importe total da caixa 1: ",importe_por_caixa(caixa1))
print("Importe total da caixa 2: ",importe_por_caixa(caixa2))
print("Importe total da caixa 3: ",importe_por_caixa(caixa3))






























