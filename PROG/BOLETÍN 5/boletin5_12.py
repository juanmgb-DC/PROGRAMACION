def main():
    total_traballadores = 0
    entre_1000_1750 = 0
    menos_de_1000 = 0

    while True:
        try:
            soldo = float(input("Introduce o soldo do traballador (0 para rematar): "))

            if soldo < 0:
                print("ERRO: O soldo non pode ser negativo.")
                continue
            elif soldo == 0:
                break

            total_traballadores += 1

            if 1000 <= soldo <= 1750:
                entre_1000_1750 += 1
            elif soldo < 1000:
                menos_de_1000 += 1

        except ValueError:
            print("Entrada non válida. Por favor, introduce un número.")

    print("\n--- RESULTADOS ---")
    print(f"Número de traballadores que ganan entre 1000 € e 1750 €: {entre_1000_1750}")

    if total_traballadores > 0:
        porcentaxe_menos_de_1000 = (menos_de_1000 / total_traballadores) * 100
        print(f"Porcentaxe de traballadores que ganan menos de 1000 €: {porcentaxe_menos_de_1000:.2f}%")
    else:
        print("Non se introduciron soldos válidos.")

if __name__ == "__main__":
    main()