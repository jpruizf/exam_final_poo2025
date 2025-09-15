from clase_nodo import Nodo
from clase_individual import Individual
from clase_equipo import Equipo
import csv
class GestorJugador:
    __comienzo:Nodo
    __tope:int

    def __init__(self):
        self.__comienzo = None
        self.__tope = 0
    
    def agregarJugadores(self,UnJugador):
        nodo = Nodo(UnJugador)
        if self.__comienzo is None:
            nodo.getSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__tope += 1
    
    def jugadores_csv(self):
        bandera = False
        bonificacion = 0
        with open('Jugadores.csv') as archivo_jugadores:
            lector = csv.reader(archivo_jugadores)
            for fila in lector:
                if not bandera:
                    bandera = True
                else:
                    tipo = fila[0]
                    nickname = fila[1]
                    juego = fila[2]
                    nivel = fila[3]
                    if nivel.lower() is 'principiante':
                        baseNivel = 100
                    elif nivel.lower() is 'intermedio':
                        baseNivel = 200
                    elif nivel.lower() is 'profesional':
                        baseNivel = 300
                    if isinstance(tipo,Individual):
                        control = fila[4]
                        torneos = int(fila[5])
                        rendimiento = int(fila[6])
                        UnJugador = Individual(control,torneos,rendimiento,**{'nickname':nickname,'juego':juego,'nivel':nivel,'baseNivel':baseNivel})
                        self.agregarJugadores(UnJugador)
                    elif isinstance(tipo,Equipo):
                        rol = fila[4]
                        if rol.lower() is 'lider':
                            bonificacion += 100
                        elif rol.lower() is 'atancante':
                            bonificacion += 75
                        elif rol.lower() is 'defensor':
                            bonificacion += 60
                        elif rol.lower() is 'soporte':
                            bonificacion += 50
                        UnJugador = Equipo(rol,bonificacion,**{'nickname':nickname,'juego':juego,'nivel':nivel,'baseNivel':baseNivel})
                        self.agregarJugadores(UnJugador)
                    else:
                        raise ValueError('El dato no es del tipo Jugador')
    def mostrarNickName(self,puntaje):
        aux = self.__comienzo
        while aux is not None:
            if aux.getDato().calculo_puntaje() >= puntaje:
                print(aux.getDato().getNickname())
            aux = aux.getSiguiente()

    def mostrarJugadores(self):
        aux = self.__comienzo
        while aux is not None:
            print(aux.getDato().getNickname(),aux.getDato().getTipo(),aux.getDato().calculo_puntaje())
            aux = aux.getSiguiente()
    
    def buscarJugadorEquipo(self,nickname,E):
        aux = self.__comienzo
        encontrado = None
        while aux is not None:
            datos_jugador = aux.getDato()
            if isinstance(datos_jugador,Equipo):
                if datos_jugador.getNickname() is not nickname:
                    raise ValueError(f'{nickname} no se ha encontrado en la coleccion')
                else:
                    encontrado = datos_jugador.getNickname()
                    E.mostrarHistorial(encontrado)
                    print(datos_jugador.getRol(),datos_jugador.calculo_puntaje())
            else:
                print(type(datos_jugador))
                raise ValueError('El dato no es del tipo jugador en Equipo')
            aux = aux.getSiguiente()
    
    def insertarJugador(self,posicion,UnJugador):
        nuevo = Nodo(UnJugador)
        aux = self.__comienzo
        anterior = self.__comienzo
        while aux is not None and posicion < self.__tope:
            anterior = aux
            if posicion >= 0 and aux.getDato().getNickname is True:
                anterior.setSiguiente(nuevo)
                nuevo.setSiguiente(aux)
                print('Dato insertado en la posicion ingrasada')
            aux = aux.getSiguiente() 