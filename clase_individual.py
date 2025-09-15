from clase_jugador import Jugador

class Individual(Jugador):
    __control:str
    __torneos_ganados:int
    __reacciones_minuto:int

    def __init__(self,control,torneos,reacciones,**kwargs):
        super().__init__(**kwargs)
        self.__control = control
        self.__torneos_ganados = torneos
        self.__reacciones_minuto = reacciones

    def getTorneos(self):
        return self.__torneos_ganados
    
    def getReacciones(self):
        return self.__reacciones_minuto
    
    def getControl(self):
        return self.__control
    
    def calculo_puntaje(self):
        return super().getBasePorNivel() + (self.getTorneos() * 50) + (self.getReacciones() * 2)