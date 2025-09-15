from clase_jugador import Jugador
class Nodo:
    __jugador:Jugador
    __siguiente:object

    def __init__(self,UnJugador):
        self.__jugador = UnJugador
        self.__siguiente = None

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__jugador