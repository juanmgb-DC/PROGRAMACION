import pickle

class Cliente:
    def __init__(self, id, nome, tel):
        self.id = id
        self.nome = nome
        self.tel = tel

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Tel: {self.tel}"


clientes = []


def cargar_datos():
    global clientes
    try:
        with open("clientes.dat", "rb") as f:
            clientes = pickle.load(f)
    except FileNotFoundError:
        clientes = []


def gardar_datos():
    with open("clientes.dat", "wb") as f:
        pickle.dump(clientes, f)


def engadir_cliente():
    print("\n--- Engadindo cliente ---")
    id = input("Id do cliente: ")
    for c in clientes:
        if c.id == id:
            print("Erro: xa existe un cliente con ese ID!")
            return
    nome = input("Nome do cliente: ")
    tel = input("Teléfono do cliente: ")
    cliente = Cliente(id, nome, tel)
    clientes.append(cliente)
    print("Cliente engadido correctamente.")


def listar_clientes():
    print("\n--- Lista de Clientes ---")
    if not clientes:
        print("Non hai clientes rexistrados.")
        return
    for c in clientes:
        print(c)


def modificar_cliente():
    print("\n--- Modificar Cliente ---")
    id_buscar = input("Introduce o ID do cliente a modificar: ")
    for c in clientes:
        if c.id == id_buscar:
            c.nome = input("Novo nome: ")
            c.tel = input("Novo teléfono: ")
            print("Cliente modificado correctamente.")
            return
    print("Cliente non atopado.")


def eliminar_cliente():
    print("\n--- Dar de baixa Cliente ---")
    id_buscar = input("Introduce o ID do cliente a eliminar: ")
    for c in clientes:
        if c.id == id_buscar:
            clientes.remove(c)
            print("Cliente eliminado correctamente.")
            return
    print("Cliente non atopado.")


def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Engadir cliente")
        print("2. Modificar cliente")
        print("3. Dar de baixa cliente")
        print("4. Listar clientes")
        print("5. Saír")
        opcion = input("Escolla unha opción: ")

        if opcion == "1":
            engadir_cliente()
        elif opcion == "2":
            modificar_cliente()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            listar_clientes()
        elif opcion == "5":
            gardar_datos()
            print("Datos gardados. Saíndo do programa...")
            break
        else:
            print("Opción non válida. Tente de novo.")


if __name__ == "__main__":
    cargar_datos()
    menu()