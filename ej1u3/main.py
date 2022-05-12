from menu import menuu

if __name__=='__main__':
    bandera = False
    m=menuu()
    while not bandera:
        print("")
        print("a Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad. ")
        print("b Dado el nombre de una carrera, mostrar código, nombre y localidad de la facultad donde esta se dicta. ")
        print("e para salir")
        opcion= input("Ingrese una opción: ")
        m.opcion(opcion)
        bandera =(opcion)=='e'