ficheiro = open('notas.txt','w')

ficheiro.write("Hola soy Juan\n")
ficheiro.write("Estoy estudiando DAM")


ficheiro.close()

ficheiro = open('notas.txt','r')
lectura = ficheiro.read()
ficheiro.close()


def buscar_notas():
    palabra = input("Introduce a palabra clave: ").lower()
    atopadas = False

    try:
        with open("notas.txt", "r", encoding="utf-8") as ficheiro:
            for i, nota in enumerate(ficheiro, start=1):
                if palabra in nota.lower():
                    print(f"✔ Nota {i}: {nota.strip()}")
                    atopadas = True

        if not atopadas:
            print("❌ Non se atoparon notas con esa palabra.")
    except FileNotFoundError:
        print("⚠ O ficheiro de notas aínda non existe.")

buscar_notas()