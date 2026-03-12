from xogador import Xogador
from partida import Partida

#3
#Clase XogoImpostor - Programa Principal
#debe realizar lo siguente 1- solicitar por teclado o numero de xogadores, 2- crear un obxecto Partida con ese numero de xogadores, 3-solicitar o nome de cada xogador, crear o obxecto Xogador correspondente e engadilo a Partida, 4- Entrar en un buble principal no que de forma repetida: solicite o nome do xogador que se vai anotar puntuacion, Solicite os puntos conseguidos nesa xogada, Engade os puntos ao xogador correspondente mediante o metodo exeitado de Partida, O bucle remata cando algun xogador acade como minimo 50 puntos 5- Tras rematar o buble, mostrar: A puntuacion final de todolos xogadores, O gañador do xogo(o xogador que primeiro alcanzou os 50 puntos). Notas debe validar que o nome introducido corresponde a un xogador existente, debe validar que os puntos introducidos son un numero enteiro positivo

class XogoImpostor:
    def __init__(self):
        self.partida = None
        self.ganador = None

    def iniciar_partida(self):
        while True:
            try:
                num_xogadores = int(input("Introduce o numero de xogadores: "))
                if num_xogadores > 6:
                    print(f"La cantidad maxima de jugadores es {self.partida.get_num_max_Xogadores()}")
                    False
                elif num_xogadores > 0:
                    break
                else:
                    print("Debe ser un numero entero positivo.")
            except ValueError:
                print("Dato invalido. Introduce un numero entero.")

        self.partida = Partida(num_xogadores)

        for i in range(num_xogadores):
            while True:
                nome = input(f"Nome do xogador {i + 1}: ")
                if nome == "":
                    print("Nombre invalido. No puede estara vacio")
                    continue

                xogador = Xogador(nome)
                indice = self.partida.addXogador(xogador)
                if indice != -1:
                    break
                print("Ya existe alguien con ese nombre. Introduce otro nombre.")

        while self.ganador is None:
            nome = input("Nome do xogador que anota puntos: ")

            xogador = self.partida.getXogador(nome)
            print(xogador)
            if xogador is None:
                print("Jugador inexistente. Introduce otro nombre.")
                continue

            try:
                puntos = int(input("Puntos conseguidos: "))
                if puntos <= 0:
                    print("Puntos invalidos. No pueden ser Negativos")
                    continue
            except ValueError:
                print("Puntos invalidos. Tiene que ser entero valido")
                continue

            try:
                total = self.partida.add_puntos_Xogador(f"{nome} {puntos}")
                print(f"Puntuacion de {nome}: {total}")

                if total >= 50:
                    self.ganador = xogador

            except XogadorNonExiste as error:
                print(error)

        print("\n FIN XOGO")
        print("Puntuación final:")
        for xog in self.partida.getXogadores():
            if xog is not None:
                print(xog)
        print(f"\n Gañador do xogo: {self.ganador.getNome()}")


if __name__ == "__main__":
    xogo = XogoImpostor()
    xogo.iniciar_partida()