class Partida:
    __nickName:str
    __nombreRival:str
    __resultado:str
    __duracion:int

    def __init__(self,nickName,nombreRival,resultado,duracion):
        self.__nickName = nickName
        self.__nombreRival = nombreRival
        self.__resultado = resultado
        self.__duracion = duracion
    
    def getNickName(self):
        return self.__nickName
    def getNombreRival(self):
        return self.__nombreRival
    
    def getResultado(self):
        return self.__resultado
    
    def getDuracion(self):
        return self.__duracion