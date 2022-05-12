class carrera:
    __codigo=''
    __nombre=''
    __duracion=''
    __titulo=''
    def __init__(self,codigo,nombre,duracion,titulo):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__duracion=duracion
        self.__titulo=titulo
        return
    def getnom(self):
        return self.__nombre
    def getduracion(self):
        return self.__duracion
    def getcode(self):
        return self.__codigo

    