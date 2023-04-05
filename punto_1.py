import numpy as np
from numpy.random import rand
import aux

#punto 1 ----------------------------------------------------------------------------------------------------------
def eliminacion_sin_pivoteo(matriz, B):
    matriz = extender_matriz(matriz, B)
    rango = range(1, len(matriz))
    for n in rango:
        modif = eliminar_sobrantes_columna(matriz, matriz[n-1], n-1)
        matriz = modif

    vector_B = []
    for fila in matriz:
        vector_B.append(fila.pop(-1))

    result = resolver_ecuaciones(matriz, vector_B)
    print(result)

def eliminar_sobrantes_columna(matriz, fila_pivot, posicion_aii):
    elemento_divisor = fila_pivot[posicion_aii]

    for n in range(posicion_aii + 1, len(matriz)):
        fila_a_modificar = matriz[n]
        elemento_modificador = fila_a_modificar[posicion_aii] / elemento_divisor
        for j in range(posicion_aii, len(fila_a_modificar)):
            fila_a_modificar[j] = fila_a_modificar[j] - (elemento_modificador * fila_pivot[j])

        matriz[n] = fila_a_modificar

    return matriz

def extender_matriz(matriz, extension):
    for n in range(len(matriz)):
        matriz[n].append(extension[n])
    return matriz

def resolver_ecuaciones(matriz, vector_B):
    x=[n for n in range(len(matriz))]
    for i in range(len(matriz) - 1, -1, -1):
        suma = 0
        for j in range(i + 1, len(matriz[i])):
            suma = suma + x[j] * matriz[i][j]
        x[i] = 1 / matriz[i][i] * (vector_B[i] - suma)

    return x

#punto 2---------------------------------------------------------------------------------------

arri = [[1,2,3,4], [1,4,9,16], [1,8,27, 64], [1 ,16, 81, 256]]
B = [2, 10, 44, 190]
eliminacion_sin_pivoteo(arri , B)