import math
import random
import numpy as np

class TablaHash:
    __arreglo = None
    __tamanio = None
    __random = None
    __cantColisiones = None
    
    def __init__(self, tamanio):
        tamanio = math.floor(tamanio/0.70)
        while not self.es_primo(tamanio):
            tamanio+=1
        self.__arreglo  = np.zeros(tamanio,dtype=int)
        self.__tamanio = math.floor(tamanio)
        self.__random = random.randint(1, self.__tamanio-1)
        self.__cantColisiones = 0

    def es_primo(self, numero):
        band = True
        n = 2
        while band and n < numero:
            if numero%n == 0:
                band = False
            else:
                n+=1
        return band
            
    def getDireccion(self, clave):
        direccion = (clave % self.__tamanio)
        return int(direccion)
        
    def insertar(self,clave):
        dir = self.getDireccion(clave)
        if self.__arreglo[dir] == 0:
            self.__arreglo[dir] = clave
        elif self.__arreglo[dir] == clave:
            print('ERROR: Elemento ya existente!')
        else:
            band = False
            i = dir
            j = (dir+self.__random)%self.__tamanio
            while not band and i != j:
                if self.__arreglo[j] == 0:
                    self.__arreglo[j] = clave
                    band = True
                elif self.__arreglo[j] == clave:
                    print('ERROR: Elemento ya existente!')
                    band = True
                else:
                    j = (j+self.__random)%self.__tamanio
    
    def buscar(self,clave):
        dir = self.getDireccion(clave)
        pos = None
        longuitud = 0
        if self.__arreglo[dir] == 0:
            print('ERROR: Elemento no existente!')
        elif self.__arreglo[dir] == clave:
            pos = dir
        else:
            i = dir
            j = (dir+self.__random)%self.__tamanio
            band = False
            while not band and i!=j:
                self.__cantColisiones+=1
                if self.__arreglo[j] == clave:
                    pos = j
                    band = True
                else:
                    j=(j+self.__random)%self.__tamanio
        return pos
                
    def getLonguitud(self):
        return self.__cantColisiones
                  
    def mostrar(self):
        for i in range(self.__tamanio):
            print(self.__arreglo[i])