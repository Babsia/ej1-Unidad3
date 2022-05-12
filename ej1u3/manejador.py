
import csv
from facultad import facultad
from carrera import carrera
class manejador:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    def cargarLista(self):
        archivo=open('Facultades.csv')
        reader=csv.reader(archivo,delimiter=',')
       
        for fila in reader:
            print(fila[5])
            cantidad=int(fila[5])
            facultad1=facultad(fila[0],fila[1],fila[2],fila[3],fila[4])
            for fila1 in reader:
                unacarrera=carrera(fila1[1],fila1[2],fila1[4],fila1[3])
                facultad1.agregarcarrera(unacarrera)
                cantidad-=1
                if cantidad==0:
                    break
            self.__lista.append(facultad1)
        
    def __str__(self):
        cadena=''
        for elemento in self.__lista:
            cadena+=('{},'.format(elemento))
        return cadena
    def buscar(self,facu):
        i = 0
        while i < len(self.__lista) and self.__lista[i].getcode() != facu:
            i += 1
        if i == len(self.__lista):
            i = -1
        return i
    
    
    
    def Listarcarreras(self):
        facu=input('ingrese un codigo de facultad: ')
        indice=self.buscar(facu)
        if indice!=-1:
            print("lo encontro")
            print('{}'.format(self.__lista[indice].getnom()))
            print("carreras:")
            self.__lista[indice].listarcarreras()
        else:
            print("no existe ese codigo de carrera")
    def buscarfacxcarrera(self):
        carrera=input("ingrese el nombre de carrera")
        for facultad in self.__lista:
            facultad.listarcarreras2(carrera)



            
