import random
from claseTablaHash import TablaHash

if __name__ == '__main__':
    objTabla = TablaHash(1000)
    lista_test = []
    for i in range(1000):
        elemento_insertar = random.randint(1000, 20000)
        objTabla.insertar(elemento_insertar)
        lista_test.append(elemento_insertar)
    for i in range(1000):
        objTabla.buscar(lista_test[i])
    print('Cantidad de colisiones: {}'.format(objTabla.getLonguitud()))
