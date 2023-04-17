import numpy as np
from numpy.random import rand

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
    return result

def eliminar_sobrantes_columna(matriz, fila_pivot, posicion_aii):
    elemento_divisor = fila_pivot[posicion_aii]
    epsilon = 1.0e-4

    #me fijo si es ld:
    if(len(matriz) != len(matriz[0])):
        print("Esta matriz es linealmente dependendiente, no presenta resultado unico")

    for n in range(posicion_aii + 1, len(matriz)):
        fila_a_modificar = matriz[n]
        elemento_modificador = fila_a_modificar[posicion_aii] / elemento_divisor

        for j in range(posicion_aii, len(fila_a_modificar)):
            fila_a_modificar[j] = fila_a_modificar[j] - (elemento_modificador * fila_pivot[j])

            if (j == posicion_aii & abs(fila_a_modificar[j]) < epsilon):
                print("Cero en la diagonal, el algoritmo de resolucion es insuficiente")

        matriz[n] = fila_a_modificar

    #me fijo si es ld (ultima fila 0, teniendo en cuenta que es cuadrada)
    if (len(matriz) == len(matriz[0]) & abs(matriz[-1][-1]) < epsilon):
        print("Esta matriz es linealmente dependendiente, no presenta resultado unico")


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
