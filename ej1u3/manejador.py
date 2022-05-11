
import csv
from facultad import facultad
class manejador:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    def cargarLista():
        lista=[]
        archivo=open('Facultades.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            if len(fila)==5:
                cantidad=int(fila[5])
            else:
                lista.append(fila)
            facultad1=facultad()


            
