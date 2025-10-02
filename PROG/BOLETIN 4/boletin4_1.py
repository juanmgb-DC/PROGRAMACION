v = float(input("As ventas anuais han sido de: "))

if v <= 100:
    print("As ventas anuais han sido de tipo baixo")
elif v > 100 and v <= 500:
    print("As ventas anuais han sido de tipo medio")
elif v > 500 and v <= 1000:
    print("As ventas anuais han sido de tipo alto")
elif v > 1000:
    print("As ventas anuais han sido de primeira necesidade")