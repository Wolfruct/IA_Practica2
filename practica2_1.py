import random
import numpy as np

def createPuzzle():
    secuencia_aleatoria = np.random.permutation(9)
    matriz_aleatoria = secuencia_aleatoria.reshape(3, 3)
    print(matriz_aleatoria)

'''''''''
def createPuzzle():
    LADO_MATRIZ=3

    matriz=[LADO_MATRIZ][LADO_MATRIZ]

    opciones = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(LADO_MATRIZ):
        for j in range(LADO_MATRIZ):
            numero = random.randint(0,len(opciones))
            matriz[i][j] = opciones[numero]
            opciones.pop(numero)riz:
            matriz[i][j] =nu
'''

class nodo:
    def __init__(self, matriz):
        self.matriz = matriz
        self.izquierda = None
        self.derecha = None

