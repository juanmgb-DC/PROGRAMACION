from xogador import Xogador

#2
# clase partida,
#Atributos: __xogadores (list[Xogador | None]): lista de participantes, __num_max_xogadores (int) : atributo que server para definir o numero maximo de xogadores que se pode crear para cada partida podese consultar o valor pero non se pode modificar, __num_xogadores (int): atributo que rexistra o numero de xogadores engadidos na lista non pode sobrepasar o __num_max_xogadores
#Contructor: recibe o numero maximo de xogadores ( num_xogadores (int)) e crea unha lista valeira
#metodos publicos: get_Xogador(nome: str) -> Xogador | None: retorna o xogador co nome indicado ou None se non existe, add_Xogador(xogador:Xogador -> int: engade un novo xogador a lista e retorna o indice onde foi colocado e se o xogador xa existe ou non hay posicions libre retorna -1, get_Xogadores()-> list[Xogador|None]: retorna a lista de xogadores, add_puntos_a_Xogador(nome_e_puntos: str) -> engade puntos ao xogador e recibe un (str) co nome do xogador e os puntos separados por un espazo ' ' ou un guion e retorna o total de puntos tras a suma ou lanza unha excepcion si o xogador non existe,
# get_Xogador_con_min_puntos(numero:int) -> Xogador | None : retorna o primeiro Xogador na lista que teña como minimo numero puntos, ou None se ningun xogador acada esa puntuacion

class Partida:
    def __init__(self,num_xogadores):
        self.__xogadores = []
        self.__num_xogadores = len(self.__xogadores)
        self.__num_max_xogadores = num_xogadores

    def getXogador(self,nome):
        for xogador in self.__xogadores:
            if xogador.getNome() == nome:
                return xogador
            else:
                return None

    def getXogadores(self):
        return self.__xogadores

    def getXogador_con_min_puntos(self,numero):
        for xogador in self.__xogadores:
            if xogador is not None and xogador.getPuntuacion() >= numero:
                return xogador
            else:
                return None

    def get_num_max_xogadores(self):
        return self.__num_max_xogadores

    def addXogador(self, xogador):
        if not isinstance(xogador,Xogador):
            return -1
        for x in self.__xogadores:
            if x is not None and x.getNome() == xogador.getNome():
               return -1
        if len(self.__xogadores) >= self.__num_max_xogadores:
            return -1
        else:
            self.__xogadores.append(xogador)

    def add_puntos_Xogador(self,nome_e_puntos:str):
        if "-" in nome_e_puntos:
            partes = nome_e_puntos.split("-")
        else:
            partes = nome_e_puntos.split(" ")

        if len(partes) != 2:
            raise ValueError ("Formato Incorrecto")

        nome = partes[0]
        puntos = int(partes[1])

        xogador = self.getXogador(nome)
        if xogador is None:
            raise XogadorNonExiste (f"O xogador {nome} non existe")

        xogador.setPuntos(puntos)
        return xogador.getPuntuacion()


class XogadorNonExiste(Exception):
    def __init__(self, mensaxe="O xogador non existe"):
        super().__init__(mensaxe)

