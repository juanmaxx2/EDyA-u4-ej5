from arbol import Arbol

if __name__ == "__main__":
    #num = int(input("\nIngrese la cantidad de pacientes"))
    num = 10
    unArbol = Arbol(num)
    
    unArbol.Insertar(4)
    unArbol.Insertar(2)
    unArbol.Insertar(6)
    unArbol.Insertar(3)
    print("\n")
    unArbol.mostrar()
    unArbol.EliminarMinimo()
    print("\n")
    unArbol.mostrar()