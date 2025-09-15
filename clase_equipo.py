from clase_jugador import Jugador
from clase_partida import Partida
import csv
class Equipo(Jugador):
    __rol:str
    __bonificacion:int
    __partidas:object
    __historial:list

    def __init__(self,rol,bonificacion,**kwargs):
        super().__init__(**kwargs)
        self.__rol = rol
        self.__bonificacion = bonificacion
        self.__historial = []

    def agregarPartida(self,UnaPartida)->None:
        self.__partidas = UnaPartida
        self.__historial.append(self.__partidas)
    
    def __delPartida__(self):
        del self.__partidas
    
    def getRol(self):
        return self.__rol
    
    def getBonificacion(self):
        return self.__bonificacion
    
    def calculo_puntaje(self):
        return super().getBasePorNivel() + 50 + 1 + self.getBonificacion()
    
    def abrir_partidas(self):
        bandera = False
        with open('Partidas.csv') as archivo_partidas:
            lector = csv.reader(archivo_partidas,delimiter=';')
            for fila in lector:
                if not bandera:
                    bandera = True
                else:
                    nickname = fila[0]
                    nombreRival = fila[1]
                    resultado = fila[2]
                    duracion = int(fila[3])
                    UnPartida = Partida(nickname,nombreRival,resultado,duracion)
                    self.agregarPartida(UnPartida)
    def mostrarHistorial(self,encontrado):
        for indice,fila in enumerate(self.__historial):
            if encontrado is fila.getNickName():
                print(fila)