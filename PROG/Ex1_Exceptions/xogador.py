# Descripcion xeral:
# queremos desenvolver un pequeno sistema para xestionar xogos simples entre varios xogadores. O programa estara organizado en 3 modulos:
# 1 xogador.py : conten a clase Xogador, 2 partida.py : conten a clase Partida, 3 game_guess.py: conten o programa principal, 4 xogadorNonExisteError.py: define o un tipo de erro
#


#1
# Clase Xogador:
# Atributos: __nome (verificar str): nome identificador do xogador. Es privado y no modificable tras la creacion del objeto.        __puntuacion: puntuacion actual del jugador. Es privado
# Constuctor: Recibe unicamente el nombre (str) e inicializa la puntuacion a 0
# Metodos publicos: get_Nome que devuleve el nombre del jugador, get_Puntuacion que devuelve la puntuacion actual, set_puntos suma puntos a puntuacion xogador
#metodos especiais: __str__


class Xogador:
    def __init__(self,nome):
        self.setNome(nome)
        self.__puntuacion = 0

    def setNome(self,nome):
        if not isinstance(nome,str):
            raise TypeError ("El nombre debe ser una cadena de texto")
        else:
            self.__nome = nome

    def setPuntos(self,p :int):
        if not isinstance(p,int):
            raise TypeError ("La puntuacion debe ser un numero entero")
        else:
            self.__puntuacion += p

    def getNome(self):
        return self.__nome

    def getPuntuacion(self):
        return self.__puntuacion

    def __str__(self):
        return f"Nombre: {self.__nome} - Puntos: {self.__puntuacion}"

    def __repr__(self):
        return self.__str__()


