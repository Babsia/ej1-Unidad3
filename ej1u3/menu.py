from manejador import manejador
class menuu:
    __switcher=None
    __M=None

    def __init__(self):
        self.__switcher = { 
            'a':self.opcion1,
            'b':self.opcion2,
            'c':self.opcion3,
            'd':self.opcion4,
            'e':self.salir
            }
        self.__M=manejador()
        self.__M.cargarLista()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')

    def opcion1(self):
        print("opcion a")
        self.__M.Listarcarreras()
        
    def opcion2(self):
        print("opcion b")
        self.__M.buscarfacxcarrera()
        
        
        
    def opcion3(self):
        print("C")
        
    def opcion4(self):
        print ('opcion d')
        