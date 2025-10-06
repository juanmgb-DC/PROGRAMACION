n1= int(input("Escriba o primeiro número da lista: "))
n2= int(input("Escriba o último número da lista: "))

for i in range(n1,n2 + 1):
    if i % 2 == 0:
        print(i)