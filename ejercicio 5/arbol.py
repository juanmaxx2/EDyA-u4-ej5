import numpy as np
import math

class Arbol:
    __item = None
    __dimension = None

    def __init__(self, dimension):
        self.__item = np.empty(dimension, dtype = int)
        self.__dimension = dimension
        self.__item[0] = 0
    
    def Insertar(self, item):
        self.__item[self.__item[0]+1] = item
        actual = self.__item[0]+1
        padre = math.floor(actual/2)
        while padre != 0 and self.__item[padre] > self.__item[actual]:
            aux = self.__item[padre]
            self.__item[padre] = self.__item[actual]
            self.__item[actual] = aux
            actual = padre
            padre = math.floor(actual/2)
        self.__item[0] += 1

    def mostrar(self): 
        for i in range(1, self.__item[0]+1):
            print(self.__item[i])

    def EliminarMinimo(self):
        self.__item[1] = self.__item[self.__item[0]]
        self.__item[0] -= 1
        i = 1
        while i < self.__item[0]:
            hijoIzq = i*2
            hijoDer = (i*2)+1 
            if self.__item[hijoIzq] < self.__item[i] and hijoIzq <= self.__item[0]:
                aux = self.__item[hijoIzq]
                self.__item[hijoIzq] = self.__item[i]
                self.__item[i] = aux
            if self.__item[hijoDer] < self.__item[i] and hijoDer <= self.__item[0]:
                aux = self.__item[hijoDer]
                self.__item[hijoDer] = self.__item[i]
                self.__item[i] = aux
            i += 1

    def getDim(self):
        return self.__dimension