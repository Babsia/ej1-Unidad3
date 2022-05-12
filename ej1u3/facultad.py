from ast import Return
from carrera import carrera


class facultad:
    __code=''
    __nombre=''
    __dir=''
    __localidad=''
    __telefono=''
    __lista=[]
    def __init__(self,code,nombre,dir,localidad,telefon):
        self.__code=code
        self.__nombre=nombre
        self.__dir=dir
        self.__localidad=localidad
        self.__telefono=telefon
        self.__lista=[]
        pass
    def agregarcarrera(self,carrera):
        self.__lista.append(carrera)
    def __str__(self):
        return ('{}'.format(self.__nombre))
    def getcode(self):
        return self.__code
    def getnom(self):
        return self.__nombre
    def listarcarreras(self):
        for carrera in self.__lista:
            print('{} '.format(carrera.getnom()))
            print("duracion:{} \n".format(carrera.getduracion()))
    def buscarcarrera(self,id):
        i = 0
        while i < len(self.__lista) and self.__lista[i].getnom() != id:
            i += 1
        if i == len(self.__lista):
            i = -1
        return i
    def listarcarreras2(self,nom):
        indice=self.buscarcarrera(nom)
        if indice !=-1:
            print("codigo de carrera:{}{}".format(self.__lista[indice].getcode(),self.getcode()))
            

    
        
    