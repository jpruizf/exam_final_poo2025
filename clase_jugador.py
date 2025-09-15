import abc
from abc import ABC,abstractmethod
class Jugador(ABC):
    __nickname:str
    __juego:str
    __nivel:str
    __base_por_nivel:int
    __origen='Argentina'
    @classmethod
    def getOrigen(cls):
        return cls.__origen
    
    def __init__(self,nickname,juego,nivel,basePorNivel):
        self.__nickname = nickname
        self.__juego = juego
        self.__nivel = nivel
        self.__base_por_nivel = basePorNivel
    
    def getTipo(self):
        return type((self).__name__)
    def getNickname(self):
        return self.__nickname
    
    def getJuego(self):
        return self.__juego
    
    def getNivel(self):
        return self.__nivel
    
    def getBasePorNivel(self):
        return self.__base_por_nivel
    
    @abstractmethod
    def calculo_puntaje(self):
        pass