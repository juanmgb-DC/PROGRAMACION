def main():
    try:
        a = float(input("Introduce o primeiro número (a):"))
        b = float(input("Introduce o segundo número (b):"))
    except ValueError:
        print("Erro: introduce un número válido.")
        return

    suma = a + b
    resta = a - b
    produto = a * b

    print(f"\nResultados para a = {a}, b = {b}:")
    print(f" Suma:     {a} + {b} = {suma}")
    print(f" Resta:    {a} - {b} = {resta}")
    print(f" Produto:  {a} * {b} = {produto}")

    if b == 0:
        print(" Cociente: Erro — división por 0 (non se pode dividir por 0).")
    else:
        cociente = a / b
        print(f" Cociente: {a} / {b} = {cociente}")

if __name__ == "__main__":
    main()

