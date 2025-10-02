#Utiliza o programa anterior para xerar unha táboa de conversión de temperaturas,
# dende 0º F ata 120º F, de 10 en 10.


tFahrenheit=0

for tFahrenheit in range (0,121, 10):
    tC = (5/9)*(tFahrenheit - 32)
    print(tFahrenheit, tC)



