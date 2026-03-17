import pickle

class Tarefa:
    fichero = "tarefas.dat"

    def __init__(self, nombre, descripcion, data, hora, duracion, estado=False):
        self.nombre = nombre
        self.descripcion = descripcion
        self.data = data
        self.hora = hora
        self.duracion = duracion
        self.estado = estado

    def __str__(self):
        return f"{self.nombre} | {self.descripcion} | {self.data} {self.hora} | {self.duracion} min | {'Feita' if self.estado else 'Pendente'}"

    @staticmethod
    def cargar_tarefas():
        try:
            with open(Tarefa.fichero, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    @staticmethod
    def gardar_tarefas(tarefas):
        with open(Tarefa.fichero, "wb") as f:
            pickle.dump(tarefas, f)

    @staticmethod
    def engadir_tarefa():
        tarefas = Tarefa.cargar_tarefas()

        nome = input("Nome da tarefa: ")
        descricion = input("Descrición: ")
        data = input("Data: ")
        hora = input("Hora: ")
        duracion = int(input("Duración en minutos: "))

        tarefa1 = Tarefa(nome, descricion, data, hora, duracion)
        tarefas.append(tarefa1)

        Tarefa.gardar_tarefas(tarefas)
        print("Tarefa engadida.")

    @staticmethod
    def listar_tarefas():
        tarefas = Tarefa.cargar_tarefas()

        if not tarefas:
            print("Non hai tarefas.")
            return

        for i, t in enumerate(tarefas):
            print(f"\nID {i}")
            print(t)