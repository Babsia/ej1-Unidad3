from ast import Return
from carrera import carrera


class facultad:
    __code=''
    __nombre=''
    __dir=''
    __localidad=''
    __telefono=''
    __lista=[]
    def __init__(self,code,nombre,dir,localidad,telefon,lista=[]):
        self.__code=code
        self.__nombre=nombre
        self.__dir=dir
        self.__localidad=localidad
        self.__telefono=telefon
        self.__lista=lista
        pass
    def agregarcarrera(self,id):
        self.__lista.append(carrera)
    def __str__(self):
        return ('{}'.format(self.__nombre))
        
    