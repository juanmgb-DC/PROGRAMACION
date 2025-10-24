#Supermercado
#Caixas - Cartos en efectivo
#Efectivo =[[(50,13),(20,5),(0'5,12),(0,23,13)]
#App que me de o importe por caixa e o total
from locale import locale_encoding_alias

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
           break
mostrarContidoUnhaCaixa('1',efectivo)




def calculoTotalEfectivoPorCaixa(caixa,totalEfectivoCaixas):
  totalEfectivo= 0
  for contidoCaixa in totalEfectivoCaixas:
      if contidoCaixa[0] == caixa:
          for i in range (1,len(contidoCaixa)):
              totalEfectivo = totalEfectivo + contidoCaixa[i][0] * contidoCaixa[i][1]
          break
  return  totalEfectivo


print(calculoTotalEfectivoPorCaixa('1',efectivo))


def calculoTotalEfectivo(totalEfectivoCaixas):
    totalEfectivo= 0
    for contidoCaixa in totalEfectivoCaixas:
        for i in range (1,len(contidoCaixa)):
            totalEfectivo= totalEfectivo + contidoCaixa[i][0] * contidoCaixa[i][1]
    return totalEfectivo

print(calculoTotalEfectivo(efectivo))


def calculoTotalMoedeiro(totalMoedeiroCaixas):
    totalMoedeiro= 0
    for contidoCaixa in totalMoedeiroCaixas:
        for i in range (1,len(contidoCaixa)):
            totalMoedeiro= totalMoedeiro + contidoCaixa[i]
    return totalMoedeiro



def mostrarMoedeiro(totalEfectivoCaixas):
    moedeiroTotal= ["total"]
    for caixa in totalEfectivoCaixas:
        for i in range (1,len(caixa)):
         haiMoedaBillete = False
         for j in range (1,len(moedeiroTotal)):
            if caixa[i][0] == moedeiroTotal[j][0]:
                moedeiroTotal[j][1] = moedeiroTotal[j][1] + caixa[i][1]
                haiMoedaBillete = True
                print("Aumento cantidade moedas ou billetes")
         if not haiMoedaBillete:
            moedeiroTotal.append(caixa[i])
            print("Engado billete ou moeda")
    print(moedeiroTotal)
    mostrarContidoUnhaCaixa("total",[moedeiroTotal])

mostrarMoedeiro(efectivo)


def menuPrincipal(totalEfectivoCaixa):
    opcion= 0
    while opcion !=5:
        print("Opcions")
        print("1. Calcula o efectivo dunha caixa")
        print("2. Calcula o total de efectivo do supermercado")
        print("3. Mostra o contido dunha caixa")
        print("4. Mostra o contido de todas as caixas")
        print("5. Sair")
        opcion = int(input("Ingresa unha opción:"))
        if opcion == 1:
            caixa = input("Introduce unha caixa")
            totalEfectivo= calculoTotalEfectivoPorCaixa(caixa,efectivo)
            print("O total da caixa", caixa, " é ", str(totalEfectivo))
        elif opcion == 2:
            totalEfectivo = calculoTotalEfectivo((efectivo))
            print("O total é: ",str(totalEfectivo))
        elif opcion == 3:
            caixa = input("Introduce unha caixa")
            mostrarContidoUnhaCaixa(caixa,efectivo)
        elif opcion == 4:
            mostrarMoedeiro(efectivo)
    print("Grazas por usar a nosa aplicacion. Ata pronto!")

menuPrincipal(efectivo)












